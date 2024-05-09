import logging

from glyphspkg.filenames import userNameToFileName
from glyphspkg.paths import build_output_file_path
from glyphspkg.plist import parse_plist_from_path, save_to_plist_path
from pathlib import Path
from typing import Any, Dict, List, Optional, Union


logger = logging.getLogger(__name__)


def package_to_single(input_path: Path, output_path: Optional[Path] = None) -> Path:
    # The main dict
    glyphs_file = convert_fontinfo(input_path)

    # Glyph order, is used to read individual glyphs files
    glyph_order = convert_order(input_path)

    # All glyphs files derived from the Glyph order list
    glyphs = []
    for glyph_name in glyph_order:
        file_name = userNameToFileName(glyph_name)
        file_path = input_path / "glyphs" / f"{file_name}.glyph"
        if not file_path.is_file():
            logger.warning(
                f"Glyph file not found for glyph '{glyph_name}': "
                f"{file_name}, glyph will be missing in converted file."
            )
            continue

        glyph = parse_plist_from_path(file_path)
        glyphs.append(glyph)

    glyphs_file["glyphs"] = glyphs

    # UIState, current display strings
    uistate = convert_uistate(input_path)
    if uistate:
        # Why the different key casing?
        glyphs_file["DisplayStrings"] = uistate["displayStrings"]

    output_file_path = build_output_file_path(input_path, output_path)
    if input_path == output_file_path:
        logger.error(f"Saving would overwrite the input file {input_path}")
        raise FileExistsError

    logger.info(f"Saving: {output_file_path}")
    save_to_plist_path(glyphs_file, output_file_path)
    return output_file_path


def convert_fontinfo(input_path: Path) -> Union[Dict[Any, Any], List[Any]]:
    return parse_plist_from_path(input_path / "fontinfo.plist")


def convert_order(input_path: Path) -> Union[Dict[Any, Any], List[Any]]:
    return parse_plist_from_path(input_path / "order.plist")


def convert_uistate(input_path: Path) -> Union[Dict[Any, Any], List[Any]]:
    uistate_path = input_path / "UIState.plist"
    if not uistate_path.is_file():
        return {}

    return parse_plist_from_path(uistate_path)
