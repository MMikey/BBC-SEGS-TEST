class Hand():
    def __init__(self):
        self.cards = {}
        self.score = 0
        
    def hit(self, next_card : tuple) -> bool:
        ''' Gets next card as tuple to add to dictionary.
        Returns true if hand still valid '''

        self.cards[ next_card[0] ] = next_card[1] # add new card to current hand

        if not(self.is_valid()):
            return self._check_aces()
        return True       

    
    def _check_aces(self) -> bool:
        ''' Loops through each card checking for aces equal to 11.
        Changes aces to 1 until hand is valid.
        Assumes that aces values are changed automatically, instead of asking user
        '''
        for card in self.cards:
            if card[0] == 'A' and self.cards[card] == 11: # check card is an Ace and value is 11
                # change ace value to 1 and check score again
                self.cards[card] = 1
                self.calculate_score
                if self.is_valid: 
                    return True
        
        return False
    
    def calculate_score(self) -> int:
        ''' Calculate score from dictionary values'''
        self.score = 0
        for card in self.cards:
            self.score += self.cards[card]
        
        return self.score

    def is_valid(self) -> bool:
        self.calculate_score()
        return self.score <= 21

    def print_hand(self) -> None:
        print("\n---- Current Hand ----")
        for card in self.cards:
            print(card, end=' ')
        print("\n----------------------")
