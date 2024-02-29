import pytest
from ..math_series.series import fibonacci, fibonacci2, lucas, sum_series

# Fibonacci Tests

# 0 - starting term in fibonacci series
def test_fibonacci_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci2_one():
    actual = fibonacci2(0)
    expected = 0
    assert actual == expected


# 1 - first term in fibonacci series
def test_fibonacci_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci2_two():
    actual = fibonacci2(1)
    expected = 1
    assert actual == expected


# 0 + 1 = 1 - sum of previous two terms, term 0 & term 1 in fibonacci series
def test_fibonacci_three():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci2_three():
    actual = fibonacci2(2)
    expected = 1
    assert actual == expected


# 1 + 1 = 2, sum of term 1 & term 2 in fibonacci series
def test_fibonacci_four():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci2_four():
    actual = fibonacci2(3)
    expected = 2
    assert actual == expected

# 5 + 8 = 13, sum of term 6 & term 5 in fibonacci series
def test_fibonacci_five():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

def test_fibonacci2_five():
    actual = fibonacci2(7)
    expected = 13
    assert actual == expected


def test_fibonacci_big_number():
    actual = fibonacci(250), fibonacci2(250)
    expected = 7896325765257458459393801417807495891023947183947776
    assert actual == expected

# Lucas Tests

# starting term in lucas is 2
def test_lucas_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected

# first term in lucas is 1
def test_lucas_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected

# 2 + 1, starting term plus first term in lucas series
def test_lucas_three():
    actual = lucas(2)
    expected = 3
    assert actual == expected

# 11 + 18 = 29, 5th term plus 6th term in lucas series
def test_lucas_four():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_lucas_big_number():
    actual = lucas(250)
    expected = 17656721319717734662791328845675730903632844218828123
    assert actual == expected

# Sum series function

#test for fibonacci AND no optional params
def test_sum_series_one():
    actual = sum_series(0)
    expected = 0
    assert actual == expected, "running 0 with no optional params should return starting term of fibonacci"

def test_sum_series_two():
    actual = sum_series(1)
    expected = 1
    assert actual == expected, "running 1 with no optional params should return first term of fibonacci"

def test_sum_series_three():
    actual = sum_series(7)
    expected = 13
    assert actual == expected, "running 7 with no optional params should return seventh term of fibonacci"

# tests for fibonacci with params
def test_sum_series_four():
    actual = sum_series(6, 0, 1)
    expected = 8
    assert actual == expected, "running 6 with fibonacci params in order should return 6th term of fibonacci"

def test_sum_series_five():
    actual = sum_series(0, 0, 1)
    expected = 0
    assert actual == expected, "running 0 with fibonacci params in order should return starting term of fibonacci"

def test_sum_series_six():
    actual = sum_series(1, 0, 1)
    expected = 0
    assert actual == expected, "running 1 with fibonacci params in order should return first term of fibonacci"

# tests lucas params
def test_sum_series_seven():
    actual = sum_series(6, 2, 1)
    expected = 18
    assert actual == expected, "running 6 with lucas params in order should return 6th term of lucas series"

def test_sum_series_eight():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected, "running 0 with lucas params in order should return starting term of lucas series"

def test_sum_series_nine():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected, "running 1 with fibonacci params in order should return first term of lucas"

# tests other starting numbers following same logic
def test_sum_series_ten():
    actual = sum_series(0, 3, 2)
    expected = 3
    assert actual == expected, "starting term should be first defined param"

def test_sum_series_eleven():
    actual = sum_series(0, 3, 2)
    expected = 2
    assert actual == expected, "first term should be second defined param"

def test_sum_series_twelve():
    actual = sum_series(4, 3, 2)
    expected = 12
    assert actual == expected, "should follow series formula of sum of two previous terms"

# test cases for float numbers

def test_sum_series_float_numbers():
    with pytest.raises(TypeError):
        sum_series(3, 0.33, 1.3), "Test numbers should be whole numbers"

def test_lucas_float_numbers():
    with pytest.raises(TypeError):
        lucas(3, 0.33, 1.3), "Test numbers should be whole numbers"

def test_fibonacci_float_numbers():
    with pytest.raises(TypeError):
        fibonacci(3, 0.33, 1.3), "Test numbers should be whole numbers"
        fibonacci2(3, 0.33, 1.3), "Test numbers should be whole numbers"
