import unittest
from unittest.mock import patch
from src.hand import Hand
from src.deck import Deck

class HandTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.hand = Hand()
        self.deck = Deck()
        
    def tearDown(self):  # this method will be run after each tests
        self.hand.cards = {}
    
    def test_hit(self):
        with patch.dict(self.hand.cards, {"5D" : 5, "5S" : 5}):
            first_score = self.hand.calculate_score()
            self.hand.hit(self.deck.get_card('2C'))
            second_score = self.hand.calculate_score()

            with self.subTest():
                self.assertGreater(second_score, first_score)
            with self.subTest():
                self.assertEqual(len(self.hand.cards), 3)

    def test_valid(self):
        with patch.dict(self.hand.cards, {"5D" : 5, "5S" : 5}):
            self.hand.hit(self.deck.get_card('5C'))
            valid = self.hand.is_valid()

            self.assertTrue(valid)

    def test_not_valid(self):
        with patch.dict(self.hand.cards, {"KD" : 10, "QS" : 10}):
            self.hand.hit(self.deck.get_card('2C'))
            valid = self.hand.is_valid()
            self.assertFalse(valid)
    
    def test_king_ace(self):
        self.hand.cards = {}
        with patch.dict(self.hand.cards, {"KS" : 10, "AS" : 11}):
            score = self.hand.calculate_score()
            self.assertEqual(score, 21)

    def test_king_queen_ace(self):
        self.hand.cards = {}
        with patch.dict(self.hand.cards, {"KS" : 10, "QS" : 10}):
            self.hand.hit(self.deck.get_card('AS'))
            score = self.hand.calculate_score()
            self.assertEqual(score, 21)

    def test_nine_ace_ace(self):
        self.hand.cards = {}
        with patch.dict(self.hand.cards, {"9S" : 9, "AS" : 11}):
            self.hand.hit(self.deck.get_card('AC'))
            score = self.hand.calculate_score()

            self.assertEqual(score,21)

if __name__ == '__main__':
    unittest.main()
