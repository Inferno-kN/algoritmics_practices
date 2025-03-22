import pytest
from hw_1.task_2 import fibonacci

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (5, [0, 1, 1, 2, 3, 5]),
                             (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
                         ])

def test_positive(input_data, expected_result):
    assert fibonacci(input_data) == expected_result

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (-5, ValueError),
                             (-1, ValueError)
                         ])

def test_negative(input_data, expected_result):
    with pytest.raises(expected_result):
        fibonacci(input_data)