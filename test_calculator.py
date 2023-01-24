""" Tests calculator.py """

import calculator

def test_calculator_add():
    """ Tests the calculator_add function """
    assert calculator.calculator_add(4, 4) == 8
    assert calculator.calculator_add(0, 0) == 0
    assert calculator.calculator_add(0, 1) == 1
    assert calculator.calculator_add(0, -5) == -5

def test_calculator_add():
    """Tests the calculator_subtract function """
    assert calculator.calculator_subract(6,3) == 3
    # assert calculator.calculator_subract(-3, -3) == 0


