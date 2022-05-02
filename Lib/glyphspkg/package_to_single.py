from os.path import basename, dirname, isfile, join, sep
from typing import Any, Dict, List, Optional, Union
from glyphspkg.filenames import userNameToFileName
from glyphspkg.plist import parse_plist_from_path, save_to_plist_path


def package_to_single(
    input_path: str, output_path: Optional[str] = None
) -> None:
    # The main dict
    input_path = input_path.rstrip(sep)
    glyphs_file = convert_fontinfo(input_path)

    # Glyph order, is used to read individual glyphs files
    glyph_order = convert_order(input_path)

    # All glyphs files derived from the Glyph order list
    glyphs = []
    for glyph_name in glyph_order:
        file_name = userNameToFileName(glyph_name)
        file_path = join(input_path, "glyphs", f"{file_name}.glyph")
        if not isfile(file_path):
            print(
                f"WARNING: Glyph file not found for glyph '{glyph_name}': "
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

    file_name = basename(input_path)
    if "." in file_name:
        file_name = file_name.rsplit(".", 1)[0]
    file_name += ".glyphs"

    if output_path is None:
        output_path = dirname(input_path)

    output_file_path = join(output_path, file_name)
    assert input_path != output_file_path
    print(f"Saving: {output_file_path}")
    save_to_plist_path(glyphs_file, output_file_path)


def convert_fontinfo(input_path: str) -> Union[Dict[Any, Any], List[Any]]:
    fontinfo_path = join(input_path, "fontinfo.plist")
    return parse_plist_from_path(fontinfo_path)


def convert_order(input_path: str) -> Union[Dict[Any, Any], List[Any]]:
    order_path = join(input_path, "order.plist")
    return parse_plist_from_path(order_path)


def convert_uistate(input_path: str) -> Union[Dict[Any, Any], List[Any]]:
    uistate_path = join(input_path, "UIState.plist")
    if not isfile(uistate_path):
        return {}

    return parse_plist_from_path(uistate_path)
