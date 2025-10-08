#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function that multiplies a
    given float by a preset multiplier"""

    def multiply(value: float) -> float:
        """Multiply a float by the preset multiplier"""

        return value * multiplier

    return multiply
