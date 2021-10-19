import unittest
from src.easyblackjack.easyblackjack import EasyBlackjack


class TestEasyBlackjack(unittest.TestCase):
    def test_generate_cards(self):
        ebj = EasyBlackjack()

        cards = ebj.generate_cards()
        self.assertIn('card_one', cards)
        self.assertIn('card_two', cards)
        self.assertIn('points', cards)

        cards = ebj.generate_cards(False)
        self.assertNotIn('points', cards)

    def test_calculate_points(self):
        ebj = EasyBlackjack()

        self.assertEqual(17, ebj.calculate_points(['10', '7']))
        self.assertEqual(16, ebj.calculate_points(['A', 'K', '5']))
        self.assertEqual(0, ebj.calculate_points(['A', '2', 'Q', 'J']))
        self.assertEqual(19, ebj.calculate_points(['q', '8', 'a']))

        self.assertRaises(TypeError, ebj.calculate_points, 'Q')
        self.assertRaises(ValueError, ebj.calculate_points, ['5', 'Y'])


if __name__ == '__main__':
    unittest.main()