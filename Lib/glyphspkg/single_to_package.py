import logging

from glyphspkg.filenames import userNameToFileName
from glyphspkg.paths import build_output_file_path, rmdir
from glyphspkg.plist import parse_plist_from_path, save_to_plist_path
from pathlib import Path
from typing import Any, Dict, List, Optional, Union


logger = logging.getLogger(__name__)


def single_to_package(input_path: Path, output_path: Optional[Path] = None) -> Path:
    output_file_path = build_output_file_path(input_path, output_path, ".glyphspackage")
    if input_path == output_file_path:
        logger.error(f"Saving would overwrite the input file {input_path}")
        raise FileExistsError

    # The main dict
    glyphs_file = parse_plist_from_path(input_path)

    logger.info(f"Saving: {output_file_path}")

    # Remove the directory if it exists
    if output_file_path.exists():
        logger.info(f"Output file exists, overwriting: <{output_file_path}>")
        if output_file_path.is_dir():
            rmdir(output_file_path)
        else:
            output_file_path.unlink()

    # Make the directory structure
    (output_file_path / "glyphs").mkdir(parents=True)

    # Glyphs
    glyphs = glyphs_file.get("glyphs", [])
    convert_glyphs(glyphs, output_file_path)

    uistate = {"displayStrings": glyphs_file.get("DisplayStrings", [])}
    convert_uistate(uistate, output_file_path)

    # Fontinfo
    # The font info is the original glyphs file structure with the separately written
    # keys removed
    for key in ("DisplayStrings", "glyphs"):
        if key in glyphs_file:
            del glyphs_file[key]
    convert_fontinfo(glyphs_file, output_file_path)

    return output_file_path


def convert_fontinfo(
    fontinfo: Union[Dict[Any, Any], List[Any]],
    output_path: Path,
) -> None:
    save_to_plist_path(fontinfo, output_path / "fontinfo.plist")


def convert_glyphs(
    glyphs: Union[Dict[Any, Any], List[Any]],
    output_path: Path,
) -> None:
    order = []
    for glyph in glyphs:
        name = glyph["glyphname"]
        order.append(name)
        save_to_plist_path(
            glyph, output_path / "glyphs" / f"{userNameToFileName(name)}.glyph"
        )
    convert_order(order, output_path)


def convert_order(
    order: Union[Dict[Any, Any], List[Any]],
    output_path: Path,
) -> None:
    save_to_plist_path(order, output_path / "order.plist")


def convert_uistate(
    uistate: Union[Dict[Any, Any], List[Any]],
    output_path: Path,
) -> None:
    save_to_plist_path(uistate, output_path / "UIState.plist")
