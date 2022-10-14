"""
Unit tests for the calculator library
"""

import cal


class TestCalculator:

    def test_addition(self):
        assert 4 == cal.add(2, 2)


    def test_subtraction(self):
        assert 2 == cal.subtract(4, 2)


    def test_multiplication(self):
        assert 100 == cal.multiply(10, 10)
