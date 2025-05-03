import unittest

from src.homework.j_classes.class_a import die

class TestDie(unittest.TestCase):

    def test_die_roll(self):
        d = die()
        for _ in range(3): 
            d.roll()
            value = d.get_rolled_value()
            self.assertIn(value, range(1,7), f"Value [value] out of range")

if __name__ == '__main__':
    unittest.main()