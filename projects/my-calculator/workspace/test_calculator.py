import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()

//create a function to test the test_lambda functions
def test_lambda(calculator):
    add = lambda self, x, y: x + y
    subtract = lambda self, x, y: x - y
    multiply = lambda self, x, y: x * y
    divide = lambda self, x, y: x / y
    exponentiate = lambda self, x, y: x ** y
    sin = lambda self, x: math.sin(math.radians(x))
    cos = lambda self, x: math.cos(math.radians(x))
    tan = lambda self, x: math.tan(math.radians(x))
    log = lambda self, x, y: math.log(y, x)

def test_addition(calculator):
    assert calculator.add(2, 3) == 5


def test_subtraction(calculator):
    assert calculator.subtract(5, 2) == 3


def test_multiplication(calculator):
    assert calculator.multiply(2, 3) == 6


def test_division(calculator):
    assert calculator.divide(6, 2) == 3


def test_division_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(6, 0)


def test_exponentiation(calculator):
    assert calculator.exponentiate(2, 3) == 8


def test_sin(calculator):
    import math
    assert calculator.sin(30) == math.sin(math.radians(30))


def test_cos(calculator):
    import math
    assert calculator.cos(60) == math.cos(math.radians(60))


def test_tan(calculator):
    import math
    assert calculator.tan(45) == math.tan(math.radians(45))


def test_log(calculator):
    import math
    assert calculator.log(10, 100) == math.log(100, 10)
