import random

class Deck:
    def __init__(self) -> None:
        self.cards = {}
        self.reset_deck()
    
    def reset_deck(self) -> None:
        '''Recreates deck as dictionary, with card:value'''
        self.suits = ['H', 'D', 'C', 'S']

        self.rank_values = {
            'A': 11, 
            'K': 10, 
            'Q': 10, 
            'J': 10, 
            '10': 10, 
            '9': 9,
            '8': 8, 
            '7': 7,
            '6': 6,
            '5': 5,
            '4': 4,
            '3': 3,
            '2': 2,
        }

        # set up cards array by concatenating each rank with every suit 
        self.cards = \
            {rank + suit: self.rank_values[rank] for suit in self.suits for rank in self.rank_values}

    def get_card(self, key : str) -> tuple:
        '''Returns a card as tuple from its key'''
        value = self.cards.get(key)
        if value == None: return None

        return (key, value)
   
    def shuffle(self) -> None:
        ''' Creates a list of keys from dictionary. Shuffle keys, overwrites current dictionary'''
        keys = list(self.cards.keys())
        random.shuffle(keys)
        self.cards = {key : self.cards[key] for key in keys}

    def draw_card(self) -> tuple:
        ''' Pops top card from the deck and returns as tuple '''
        return self.cards.popitem()
