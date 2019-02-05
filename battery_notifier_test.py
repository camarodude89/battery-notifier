import battery_notifier
from unittest import TestCase
import unittest

class Testify(TestCase):

    def test_update_battery_percentage(self):
        self.assertTrue(1 <= battery_notifier.update_battery_percentage() <= 100)

    def test_update_power_source_status(self):
        status = battery_notifier.update_power_source_status()
        print(status)
        self.assertTrue(status == 'Plugged' or status == 'Not Plugged')


if __name__ == '__main__':
    unittest.main()
