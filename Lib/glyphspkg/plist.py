import codecs
import openstep_plist

from pathlib import Path
from typing import Any, Dict, List, Union


def parse_plist_from_path(
    plist_path: Path,
) -> Union[Dict[Any, Any], List[Any]]:
    with codecs.open(str(plist_path), "rb", "utf-8") as f:
        d = f.read()
    return parse(d)


def save_to_plist_path(obj: Union[Dict[Any, Any], List[Any]], plist_path: Path) -> None:
    with codecs.open(str(plist_path), "wb", "utf-8") as f:
        openstep_plist.dump(
            obj,
            f,
            unicode_escape=False,
            indent=0,
            single_line_tuples=True,
            # TODO: The released version 0.3.1 of openstep_plist doesn't have the
            # ``escape_newlines`` argument
            # escape_newlines=False,
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
