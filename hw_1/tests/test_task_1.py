from hw_1.task_1 import factorial
import pytest

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (5, 120),
                             (2, 2)
                         ])

def test_positive(input_data, expected_result):
    assert factorial(input_data) == expected_result

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (-6, ValueError),
                             (-5, ValueError)
                         ])

def test_negative(input_data, expected_result):
    with pytest.raises(expected_result):
        factorial(input_data)

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (0, 1)
                         ])

def test_bound(input_data, expected_result):
    assert factorial(input_data) == expected_result