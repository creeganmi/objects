for number in range(2,11):  # too lazy to type 2-10 with '' & ,
    print(f"'{number}',")

class Card:
    def __init__(self, value, suit):
        self.cost = value
        self.rank = ['A','2','3','4','5','6','7','8','9','10', 'J','K'][value-1]
        self.suit = '(♣)(♦)(♥)(♠)'[suit]
        
        def price(self): # return value of card
            if self.rank >= 10: # if 10 or royal card the rank is 10
                return 10
            elif self.rank == 1:    # ace value is 11
                return 11
            return self.rank    # otherwise return value of the card

def show(self): # visualize the card!
    print('|','\u2500' * 10)
    print(f'| {self.value:<2}       |')
    
    
        print('|','\u2500' * 10)
    print(f'| {self.value:<2}       |')