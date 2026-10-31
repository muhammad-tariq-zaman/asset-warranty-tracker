import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from datetime import date
from main import status


class TestWarranty(unittest.TestCase):
    def test_expired(self):
        self.assertEqual(status(date(2026, 1, 1), date(2026, 10, 29), 90), "EXPIRED")

    def test_expiring_soon(self):
        self.assertEqual(status(date(2026, 12, 1), date(2026, 10, 29), 90), "EXPIRING SOON")

    def test_ok(self):
        self.assertEqual(status(date(2027, 6, 1), date(2026, 10, 29), 90), "OK")
