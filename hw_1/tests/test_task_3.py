import pytest
from hw_1.task_3 import count_ones

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (4, 1),
                             (5, 2)
                         ])

def test_positive(input_data, expected_result):
    assert count_ones(input_data) == expected_result

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (-1, ValueError),
                             (-8, ValueError)
                         ])

def test_negative(input_data, expected_result):
    with pytest.raises(expected_result):
        count_ones(input_data)


@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (0, 0)
                         ])

def test_bound(input_data, expected_result):
    assert count_ones(input_data) == expected_result