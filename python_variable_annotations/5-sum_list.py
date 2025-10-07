#!/usr/bin/env python3
"""defain function sum_list which takes a list input_list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list containing float numbers.

    Returns:
        float: The sum of all numbers in the list.
    """
    return float(sum(input_list))
