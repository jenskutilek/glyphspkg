from typing import Any, Dict, List, TextIO, Union


def loads(
    string: str, dict_type: type = dict, use_numbers: bool = False
) -> Union[Dict[Any, Any], List[Any]]: ...


def load(fp: TextIO, dict_type: type = dict, use_numbers: bool = False): ...


class ParseError(Exception):
    pass
