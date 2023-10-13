import unittest

from context import oop

class PointTestCase(unittest.TestCase):

    def test_set_x_positive(self):
        point = oop.Point()
        point.x = 10
        self.assertEqual(10, point.x)

    def test_set_x_negative(self):
        point = oop.Point()
        point.x = -10
        self.assertEqual(10, point.x)

    def test_dist_the_same(self):
        point1 = oop.Point()
        point2 = oop.Point()
        result = point1.distance(point2)
        self.assertEqual(0, result)

    def test_dist_result_1(self):
        point1 = oop.Point(1, 1)
        point2 = oop.Point(1, 2)
        result = point1.distance(point2)
        self.assertEqual(1, result)

    def test_dist_result_1(self):
        point1 = oop.Point(1, 1)
        point2 = oop.Point(2, 2)
        result = point1.distance(point2)
        self.assertAlmostEquals(1.414213, result, delta=0.0001)


if __name__ == '__main__':
    unittest.main()
