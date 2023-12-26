from Project_1_5B import average_temp, my_sort, power_my, power_recursive, power, sort_from_zero
import pytest


def test_average_temp():
    assert average_temp([1, 2, None, 3, 4, 5, None, -2, 8]) == 3
    
def test_sort():
    less_zero, more_zero = my_sort([10, -5, 3, -2, 0, 7, -1])
    assert less_zero == [-1, -2, -5]
    assert more_zero == [0, 3, 7, 10]
        
def test_power():
    assert power_my(5,2) == 25
    assert power_recursive(5,2) == 25
    assert power(5,2) == 25

if __name__ == '__main__':
    pytest.main()