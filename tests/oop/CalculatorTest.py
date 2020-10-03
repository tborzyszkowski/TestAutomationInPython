import unittest

from context import oop


class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = oop.Calculator()

    def test_add(self):
        self.calculator.add(1)
        self.assertEqual(self.calculator.state, 1)


if __name__ == '__main__':
    unittest.main()
