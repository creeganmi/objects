from deck import Deck

class Player:
    def __init__(self, DealerPlayer, deck): 
        self.cards = []
        self.DealerPlayer= DealerPlayer         # dealer or player
        self.deck = deck                        # each player has access to deck
        self.score = 0                          # each player starts game at 0
        
    def hit(self):                              # allows player to draw card from deck and check score
        self.cards.extend(self.deck.draw(1))
        self.check.score(1)                     
        if self.score > 21:                     # check for blackjack
            return 1                            # if not then give them card
        return 0
    
    def draw(self):                             # draw function for player to draw 2 cards
        self.cards.extend(self.deck.draw(2))
        self.check_score()                      # check score
        if self.score == 21:
            return 1
        return 0
    
    def check_score(self):                      # add up scores of all the cards and count number of aces
        ace_counter = 0
        self.score = 0
        for card in self.cards:
            if card.price() == 11:             
                ace_counter += 1
            self.score += card.price()
            
        while ace_counter != 0 and self.score > 21:   # if hand goes over 21, we can subtract 10 from each ace they have to simulate 1
            ace_counter -= 1
            self.score -= 10
        return self.score
    
    def show(self):
        if self.DealerPlayer:
            print("Dealer's Hand")
        else:
            print("Player's Hand")
            
        for i in self.cards:
            i.show()
            
        print("Score: "+str(self.score))
            
        