from parameterized import parameterized
from unittest_parametrize import ParametrizedTestCase
import unittest

from context import oop

# datasource = [(1, 1, 2), (1, 2, 3)]

class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = oop.Calculator()

    def test_add_one_to_new_calculator(self):
        self.calculator.add(1)
        self.assertEqual(1, self.calculator.state)

    def test_add_negative_number_to_new_calculator(self):
        self.calculator.add(-100)
        self.assertEqual(-100, self.calculator.state)

    def test_mult_two_times_two_gives_four(self):
        self.calculator.state = 2
        self.calculator.mult(2)
        self.assertEqual(4, self.calculator.state)

    def test_mult_two_times_zero_gives_zero(self):
        self.calculator.state = 2
        self.calculator.mult(0)
        self.assertEqual(0, self.calculator.state)

    def test_mult_two_big_numbers(self):
        self.calculator.state = 123456
        self.calculator.mult(654321)
        self.assertEqual(80779853376, self.calculator.state)

    # @parameterized.expand(
    #
    #     [
    #         [state, liczba, result]
    #         for (state, liczba, result) in datasource
    #     ],
    # )
    # def test_subtract_two_times_two_gives_four(self, state, liczba, result):
    #     self.calculator.state = state
    #     self.calculator.add(liczba)
    #     self.assertEqual(result, self.calculator.state)


if __name__ == '__main__':
    unittest.main()
