import codecs
from typing import Any, Dict, List, Union
import openstep_plist


def parse_plist_from_path(plist_path: str) -> Union[Dict[Any, Any], List[Any]]:
    with codecs.open(plist_path, "rb", "utf-8") as f:
        d = f.read()
    return parse(d)


def save_to_plist_path(
    obj: Union[Dict[Any, Any], List[Any]], plist_path: str
) -> None:
    with codecs.open(plist_path, "wb", "utf-8") as f:
        openstep_plist.dump(
            obj, f, unicode_escape=False, indent=0, single_line_tuples=True
        )


# From glyphsLib.parser
# https://github.com/googlefonts/glyphsLib
# Licensed under Apache-2.0


def parse(d: str) -> Union[Dict[Any, Any], List[Any]]:
    try:
        d = _fl7_format_clean(d)
        result: Union[Dict[Any, Any], List[Any]] = openstep_plist.loads(
            d, use_numbers=True
        )
    except openstep_plist.parser.ParseError as e:
        raise ValueError("Failed to parse file") from e
    return result


def _fl7_format_clean(d: str) -> str:
    """
    FontLab 7 glyphs source format exports include a final closing semicolon.
    This method removes the semicolon before passing the string to the parser.
    """
    # see https://github.com/googlefonts/fontmake/issues/806
    return d.rstrip(";\n")
