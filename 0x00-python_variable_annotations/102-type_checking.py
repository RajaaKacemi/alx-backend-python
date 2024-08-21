#!/usr/bin/env python3
"""Function to zoom an array by a given factor."""

from typing import List, Tuple, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Returns a list where each element """
    zoomed_in: List[int] = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = (12, 72, 91)  # Changed from list


zoom_2x = zoom_array(array) # Changed from list


zoom_3x = zoom_array(array, 3) # Changed from list
