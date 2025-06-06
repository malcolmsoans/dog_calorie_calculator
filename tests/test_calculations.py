import unittest

from dog_calories import calculate_rer, calculate_calories, size_list, age_list

class TestCalculations(unittest.TestCase):
    def test_calculate_rer_inside_range(self):
        # 10kg medium size should use 30*weight + 70
        self.assertEqual(calculate_rer(10, size_list[1]), 370.0)

    def test_calculate_rer_outside_range(self):
        # 1kg small size should use 70*(weight**0.75)
        self.assertEqual(calculate_rer(1, size_list[0]), 70.0)

    def test_calculate_calories_neutered_adult(self):
        # 10kg medium dog with age 'Normal Neutered Adult' uses multiplier 1.6
        rer = calculate_rer(10, size_list[1])
        expected = round(rer * 1.6, 2)
        self.assertEqual(calculate_calories(10, age_list[2], size_list[1]), expected)

if __name__ == '__main__':
    unittest.main()
