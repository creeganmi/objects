from deck import Deck
from player import Player

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)
        
    def play(self):
        player_status = self.player.draw()
        dealer_status = self.dealer.draw()
        
        self.player.show()
        
        if palyer_status == 1:
            print("Player's game - blackjack baby!")
            if dealer_status == 1:
                print("Tie - Dealer and Player got blackjack!")
            return 1
        
    cmd = ""                                    # this is where you play blackjack
    while cmd != "Stay":
        bust = 0
        cmd = input("Hit or Stay?")
        
        if cmd == "Hit":
            bus = self.player.hit()
            self.player.show()
        if bust == 1:
            print("Better luck next time. Player busted")
            return 1
        
        while self.dealer.check_score() < 17:            # dealer hits until they get 17 or over
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer busted. You win!")
                return 1
            self.dealer.show()
            
        if self.dealer.check_score() == self.player.check_score():
            print("Tie - oh well")
        elif self.dealer.check_score() > self.player.check_score():
            print("Dealer's game.")
        elif self.dealer.check_score() < self.player.check_score():
            print("Player wins! Congrats!")
            
b = Blackjack()
b.play()