
def numbers_multiplication_in_exponent(number1: float, number2: float, /, *, exponent: float) -> float:

    multiplication_res = number1 * number2
    exponent_res = multiplication_res ** exponent
    return exponent_res


print(numbers_multiplication_in_exponent(-2, 3, exponent=2))