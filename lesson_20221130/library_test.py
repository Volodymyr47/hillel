import pytest
from library import numbers_multiplication_exponent


right_params = [(2, 2, 2, 16), (2, -2, 3, -64), (-2, 3, 2, 36), (25, 25, 0.5, 25)]
bad_params = [(2, -2, 0.5)]


@pytest.mark.parametrize('num1, num2, exp, expected', right_params)
def test_numbers_multiplication_in_exponent(num1, num2, exp, expected):
    assert numbers_multiplication_exponent(num1, num2, exponent=exp) == expected, 'not expected result'


def test_numbers_multiplication_in_exponent_type():
    assert type(numbers_multiplication_exponent(2, -3, exponent=2)) in (float, int), 'function type error'


@pytest.mark.parametrize('num1, num2, exp', bad_params)
def test_of_converting_result_error(num1, num2, exp):
    with pytest.raises(TypeError):
        numbers_multiplication_exponent(num1, num2, exponent=exp)


def test_of_first_param_type_error():
    with pytest.raises(TypeError):
        numbers_multiplication_exponent('2', -3, exponent=2)


def test_of_second_param_type_error():
    with pytest.raises(TypeError):
        numbers_multiplication_exponent(2, '3', exponent=2)


def test_of_exponent_type_error():
    with pytest.raises(TypeError):
        numbers_multiplication_exponent(2, 3, exponent='2')


def test_value_exponent_error():
    with pytest.raises(ValueError):
        numbers_multiplication_exponent(2, 3, exponent=101)
