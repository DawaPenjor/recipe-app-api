"""
sample test
"""

from django.test import SimpleTestCase # noqa


from app import calc


class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """adding two numbers together"""
        res = calc.addition(3, 5)

        self.assertEqual(res, 8)

    def test_subtract_number(self):
        """Subtract two nhumbers"""
        res = calc.subtract(15, 10)
        self.assertEqual(res, 5)
