
import unittest
from student import calculate_total, calculate_average, check_result


class TestStudent(unittest.TestCase):

    def test_total(self):
        self.assertEqual(calculate_total(80, 70, 90), 240)

    def test_average(self):
        self.assertEqual(calculate_average(60, 70, 80), 70)

    def test_pass(self):
        self.assertEqual(check_result(75), "Pass")

    def test_fail(self):
        self.assertEqual(check_result(30), "Fail")


if __name__ == "__main__":
    unittest.main()
