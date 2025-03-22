import pytest
from hw_1.task_4 import is_palindrome


@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (121, True),
                             (434, True)
                         ])

def test_positive(input_data, expected_result):
    assert is_palindrome(input_data) == expected_result

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             ("", ValueError)
                         ])
def test_negative(input_data, expected_result):
    with pytest.raises(expected_result):
        is_palindrome(input_data)

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (7, True),
                             (4, True)
                         ])

def test_bound(input_data, expected_result):
    assert is_palindrome(input_data) == expected_result