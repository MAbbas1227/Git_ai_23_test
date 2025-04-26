import pytest
from calculator import Calculator
# At the top of your test_calculator.py file
from calculator import PreciseCalculator  # Adjust the path as needed

def test_add():
    calc = Calculator()
    assert calc.add(3, 5) == 8
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2
def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 5) == -4
    assert calc.subtract(-5, -3) == -2

def test_multiplication():
    calc=Calculator()
    assert calc.multiply(4,3)==12
    assert calc.multiply(4.3,3.2)==13.76
    assert calc.multiply(-2,-3)==6

def test_division():
    calc=Calculator()
    assert calc.divide(10,2)==5
    assert calc.divide(5,2)==2.5
    assert calc.divide(2,0)== float('inf')
    

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (3, 5, -2),
    (-2, -2, 0),
    (0, 5, -5)
])
def test_subtract_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (2.0, 3.0, 6.0),
    (-1, 5, -5),
    (0, 100, 0)
])
def test_multiply_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (9, -3, -3),
    (-8, -2, 4)
])
def test_divide_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.divide(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -2, 0.25),
    (-2, 3, -8),
    (0, 5, 0)
])
def test_power_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.power(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (3, 5, -2),
    (-2, -2, 0),
    (0, 5, -5)
])
def test_subtract_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (2.0, 3.0, 6.0),
    (-1, 5, -5),
    (0, 100, 0)
])
def test_multiply_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (9, -3, -3),
    (-8, -2, 4)
])
def test_divide_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.divide(a, b) == expected



@pytest.mark.parametrize("n, expected", [
    (0, 1),    # Edge case
    (1, 1),    # Edge case
    (5, 120),  # Normal case
    (3, 6),    # Normal case
])
def test_factorial_normal_and_edge_cases(n, expected):
    calc = Calculator()
    assert calc.factorial(n) == expected

def test_factorial_negative_case():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.factorial(-5)



@pytest.mark.parametrize("n, expected", [
    (0, 0),    # Edge case
    (1, 1),    # Edge case
    (2, 1),    # Normal case
    (3, 2),    # Normal case
    (5, 5),    # Normal case
    (6, 8),    
])
def test_fibonacci_normal_and_edge_cases(n, expected):
    calc = Calculator()
    assert calc.fibonacci(n) == expected

def test_fibonacci_negative_case():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.fibonacci(-3)
@pytest.mark.parametrize("a, b, expected, precision", [
    (1.2345, 2.3456, 3.58, 2),  # Test addition with 2 decimal precision
    (1.2345, 2.3456, 3.580, 3),  # Test addition with 3 decimal precision
    (1.23456, 2.34567, 3.580, 3),  # Test addition with 3 decimal precision (fixed)
])
def test_addition_with_precision(a, b, expected, precision):
    calc = PreciseCalculator(precision=precision)
    result = calc.add(a, b)
    assert result == expected


# Similarly, you can add tests for subtraction, multiplication, and division

@pytest.mark.parametrize("a, b, expected, precision", [
    (5.6789, 3.6789, 2.0, 2),   # Test subtraction with 2 decimal precision
    (5.6789, 3.6789, 2.000, 3),  # Test subtraction with 3 decimal precision
])
def test_subtraction_with_precision(a, b, expected, precision):
    calc = PreciseCalculator(precision=precision)
    result = calc.subtract(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected, precision", [
    (2.345, 3.2, 7.504, 3),  # Test multiplication with 3 decimal precision
    (2.345, 3.2, 7.50, 2),   # Test multiplication with 2 decimal precision
])
def test_multiplication_with_precision(a, b, expected, precision):
    calc = PreciseCalculator(precision=precision)
    result = calc.multiply(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected, precision", [
    (7.5, 2.5, 3.0, 2),  # Test division with 2 decimal precision
    (7.5, 2.5, 3.000, 3), # Test division with 3 decimal precision
])
def test_division_with_precision(a, b, expected, precision):
    calc = PreciseCalculator(precision=precision)
    result = calc.divide(a, b)
    assert result == expected