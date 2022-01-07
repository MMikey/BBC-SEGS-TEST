from src.deck import Deck
from src.hand import Hand

class Dealer:
    def __init__(self) -> None:
        self.deck = Deck()
        self.hand = Hand()
    
    def deal(self) -> None:
        ''' Shuffles the deck and deals first two cards'''
        self.deck.shuffle()
        for i in range(0,2):
            self.hand.hit(self.deck.draw_card())

    def play(self) -> None:
        self.deal()
        
        stand = False
        while not(stand):
            self.hand.print_hand()
            
            answer = input("Hit or Stand? (h/s) :") 
            if answer == "h":

                new_card = self.deck.draw_card()
                if not self.hand.hit(new_card):
                    self.hand.print_hand()
                    print("----     Bust     ----")
                    stand = True
                    continue
            elif answer == "s":
                stand = True
        
        print(f"Final total: {self.hand.calculate_score()}")




