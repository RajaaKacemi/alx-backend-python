#!/usr/bin/env python3
"""Duck typing example with correct annotations."""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence if it exists, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
