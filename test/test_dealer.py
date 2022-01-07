import unittest
from unittest.mock import patch

from src.dealer import Dealer


class DealerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.dealer = Dealer()
        
    def tearDown(self):  # this method will be run after each tests
        self.dealer.hand.cards = {}
    
    def test_opening_hand(self):  # any method beginning with 'test' will be run by unittest
        self.dealer.deal()
        number_of_cards = len(self.dealer.hand.cards)
        self.assertEqual(number_of_cards, 2)

    def test_hit(self):
        with patch('builtins.input', side_effect = ['h', 's']):
            self.dealer.play()
            number_of_cards = len(self.dealer.hand.cards)
            self.assertEqual(number_of_cards, 3)


    def test_stand(self):
        with patch('builtins.input', side_effect = ['s']):
            self.dealer.play()
            number_of_cards = len(self.dealer.hand.cards)
            self.assertEqual(number_of_cards, 2)
  

if __name__ == '__main__':
    unittest.main()
