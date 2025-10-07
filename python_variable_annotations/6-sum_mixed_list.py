#!/usr/bin/env python3
"""defain a function sum_mixed_list which takes a list mxd_lst"""


from typing import List


def sum_mixed_list(mxd_lst: list[int, float]) -> float:
    """returns their sum as a float"""

    return float(sum(mxd_lst))
