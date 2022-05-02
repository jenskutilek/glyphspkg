from typing import Any, Dict, List, Optional, TextIO, Union


def dumps(
    obj: Union[Dict[Any, Any], List[Any]],
    unicode_escape: bool = True,
    float_precision: int = 6,
    indent: Optional[int] = None,
    single_line_tuples: bool = False,
): ...


def dump(
    obj: Union[Dict[Any, Any], List[Any]],
    fp: TextIO,
    unicode_escape: bool = True,
    float_precision: int = 6,
    indent: Optional[int] = None,
    single_line_tuples: bool = False,
): ...
