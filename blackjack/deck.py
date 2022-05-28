import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []                         # initialize deck with empty list of cards
        
    def fiftytwo(self):                         # create 52 card deck
        for crd1 in range(1,14):                # loop through 52 times
            for crd2 in range(4):
                self.cards.append(Card(crd1, crd2))
                
    def draw(self, iteration):                  # randomly remove cards from deck
        cards = []                              # put cards in list so we can see them
        for crd1 in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(cards)
        return cards
    
    def count(self):                            # counts number of cards in deck
        return len(self.cards)
    