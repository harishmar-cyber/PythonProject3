
import unittest
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


class TestTemperature(unittest.TestCase):

    def test_freezing_point(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_boiling_point(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_convert_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)

    def test_room_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(25), 77)


if __name__ == "__main__":
    unittest.main()
