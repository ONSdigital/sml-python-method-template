"""
<Method_Name> <Synopsis>

For Copyright information, please see LICENCE.
"""
from typing import Union


def method_name(n: int) -> Union[int, None]:
    """Calculate the factorial of a non-negative integer"""
    if n < 0:
        # Factorial on negative numbers is not possible
        return None
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
