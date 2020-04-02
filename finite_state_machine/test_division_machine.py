import pytest

from finite_state_machine.division_machine import DivisionMachine


def test_division_machine_divide_11():
    assert DivisionMachine().evaluate('11') == 0

def test_division_machine_divide_01():
    assert DivisionMachine().evaluate('01') == 1

def test_division_machine_divide_10():
    assert DivisionMachine().evaluate('10') == 2

def test_division_machine_divide_0000():
    assert DivisionMachine().evaluate('0000') == 0

def test_division_machine_empty_string():
    assert DivisionMachine().evaluate('') == 0

def test_division_machine_non_string():
    with pytest.raises(ValueError):
        DivisionMachine().evaluate(123)

def test_division_machine_invlaid_number():
    with pytest.raises(ValueError):
        DivisionMachine().evaluate('Hello there! :)')
