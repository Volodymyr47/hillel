from typing import Union
import functools


@functools.lru_cache(maxsize=None)
def numbers_multiplication_exponent(
        number1: Union[int, float],
        number2: Union[int, float],
        /,
        *,
        exponent: Union[int, float],
) -> Union[int, float]:

    if not isinstance(number1, (int, float)):
        print('Type of argument must be integer or float')
        raise TypeError

    if not isinstance(number2, (int, float)):
        print('Type of argument must be integer or float')
        raise TypeError

    if not isinstance(exponent, (int, float)):
        print('Type of argument must be integer or float')
        raise TypeError

    if exponent > 100:
        raise ValueError

# to get the big integer resul without an error
    if number1 - int(number1) == 0:
        number1 = int(number1)

    if number2 - int(number2) == 0:
        number2 = int(number2)

    if exponent - int(exponent) == 0:
        exponent = int(exponent)

    multiplication_res = number1 * number2
    exponent_res = multiplication_res ** exponent

    if exponent_res - int(exponent_res) == 0:
        return int(exponent_res)

    return exponent_res
