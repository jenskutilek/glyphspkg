import codecs
from typing import Dict, List, Union
import openstep_plist


def parse_plist_from_path(plist_path: str) -> Union[Dict, List]:
    with codecs.open(plist_path, "rb", "utf-8") as f:
        d = f.read()
    return parse(d)


def save_to_plist_path(obj: Union[Dict, List], plist_path: str) -> None:
    with codecs.open(plist_path, "wb", "utf-8") as f:
        openstep_plist.dump(
            obj, f, unicode_escape=False, indent=0, single_line_tuples=True
        )


# From glyphsLib.parser
# https://github.com/googlefonts/glyphsLib
# Licensed under Apache-2.0


def parse(d: Union[str, bytes]) -> Union[Dict, List]:
    try:
        if isinstance(d, str):
            d = _fl7_format_clean(d)
            d = openstep_plist.loads(d, use_numbers=True)
        elif isinstance(d, bytes):
            d = _fl7_format_clean(d)
            d = openstep_plist.loads(d.decode(), use_numbers=True)
        result = d  # Do we need to parse it for our purpose?
    except openstep_plist.parser.ParseError as e:
        raise ValueError("Failed to parse file") from e
    return result


def _fl7_format_clean(d: Union[str, bytes]) -> Union[str, bytes]:
    """
    FontLab 7 glyphs source format exports include a final closing semicolon.
    This method removes the semicolon before passing the string to the parser.
    """
    # see https://github.com/googlefonts/fontmake/issues/806
    if isinstance(d, str):
        d = d.rstrip(";\n")
    elif isinstance(d, bytes):
        d = d.rstrip(b";\n")
    return d
