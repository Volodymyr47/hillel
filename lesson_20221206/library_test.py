import pytest
from library import can_be_float, get_point_from_input

params = [('2', True), ('-5.25', True), (2, True), (['5'], False), ('asd', False)]


@pytest.mark.parametrize('value, expected', params)
def test_can_be_float(value, expected):
    assert can_be_float(value) == expected, 'not expected result'


def test_get_point_from_input_type_error():
    with pytest.raises(TypeError):
        get_point_from_input('2')
