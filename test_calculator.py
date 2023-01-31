""" Tests calculator.py """

import calculator


def test_calculator_add():
    """ Tests the calculator_add function """
    assert calculator.calculator_add(4, 4) == 8
    assert calculator.calculator_add(0, 0) == 0
    assert calculator.calculator_add(0, 1) == 1
    assert calculator.calculator_add(0, -5) == -5


def test_calculator_subtract():
    """Tests the calculator_subtract function """
    assert calculator.calculator_subtract(6, 3) == 3
    assert calculator.calculator_subtract(-3, -3) == 0
    assert calculator.calculator_subtract(3,6) == -3

def test_calculator_multiply():
    """Tests the calculator_multiply function"""
    assert calculator.calculator_multiply(3,3) == 9
    assert calculator.calculator_multiply(4,0) == 0

def test_calculator_divide():
    """Tests the calculator_divide function"""
    assert calculator.calculator_divide(9,3) == 3
