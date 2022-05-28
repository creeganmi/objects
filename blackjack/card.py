# for number in range(2,11):                  # too lazy to type 2-10 with '' & ,
#     print(f"'{number}',")

class Card:
    def __init__(self, rank, suit):
        self.cost = rank
        self.rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'][rank-1]
        self.suit = '♣♦♥♠'[suit]
        
    def show(self):                         #visualize card
        print('┌───────┐')
        print(f'| {self.rank:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.rank:>2} |')
        print('└───────┘')
        
    def price(self):                    # return value of card
        if self.cost >= 10:             # if 10 or royal card the rank is 10
            return 10
        elif self.cost == 1:            # ace value is 11
            return 11
        return self.cost                # otherwise return value of the card   