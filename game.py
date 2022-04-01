#-------------------------------------------------------------------------------
# FILE NAME:      hmwk2.py
# DESCRIPTION:    uses python3 to create black jack game
# USAGE:          python3 hmwk2.py
#                 
# notes:          First time creating classes in python
#                 
#
# MODIFICATION HISTORY
# Author               Date           version
#-------------------  ------------    ---------------------------------------
# Annette McDonough   2022-02-10      1.0 first version 
# Annette McDonough   2022-02-11      1.1 adding dealer class
# Annette McDonough   2022-02-13      1.2 adding player class
# Annette McDonough   2022-02-15      1.3 working on bugs
# Annette McDonough   2022-02-18      1.4 working on doubledown
#-----------------------------------------------------------------------------

import random


class Player:
    def __init__(self, is_dealer, deck):
        """Constructor for player"""
        self.cards = []
        self.is_dealer = is_dealer
        self.deck = deck
        self.score = 0
        self.bet = 1

    def hit(self):
        """Method to take a card"""
        self.cards.extend(self.deck.draw())
        self.validate_score()
        if self.score > 21:
            return True
        return False

    def deal(self):
        """Draw two cards and check whether score is 21"""
        self.cards.extend(self.deck.draw(2))
        self.validate_score()
        if self.score == 21:
            return True
        return False

    def validate_score(self):
        """Validate the score"""
        var = 0
        self.score = 0
        for card in self.cards:
            if card.number() == 11:
                var += 1
            self.score += card.number()

        while var != 0 and self.score > 21:
            var -= 1
            self.score -= 10
        return self.score

    def show(self):
        """Show card details"""
        if self.is_dealer:
            print("Dealer's Cards")
        else:
            print("Player's Cards")

        for _ in self.cards:
            _.display_card()

        print("Score: " + str(self.score))

    def check_black_jack(self):
        """Check black jack while playing"""
        return self.score == 21



    def double_down(self):
        if self.score == 9 or self.score == 10 or self.score == 11:
            option = input("Would you like to double down? Y, N ")
            if option == 'Y':
                self.bet *= 2


             



class Deck:
    def __init__(self):
        """Constructor for Deck class"""
        self.cards = []

    def create_deck(self):
        """Generate all 52 card objects"""
        self.cards = [Card(i, j) for i in range(1, 14) for j in range(4)]

    def draw(self, it=1):
        """Draw cards default set to 1"""
        cards = []
        for i in range(it):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards


class Card:
    def __init__(self, value, suit):
        """Constructor for card class"""
        self.cost = value
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value - 1]
        self.suits = '♣♠♥♦'[suit]

    def display_card(self):
        """Display the card"""
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suits}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')

    def number(self):
        """add number based on selected card"""
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost


class Blackjack:
    def __init__(self):
        """Constructor for BlackJAck Class"""
        self.deck = Deck()
        self.deck.create_deck()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play(self):
        """Start the game"""
        player_report = self.player.deal()
        dealer_report = self.dealer.deal()

        self.player.show()

        if player_report:
            print("Player got Blackjack! Congrats!")
            if dealer_report:
                print("Dealer and Player got Blackjack! It's a Tie.")
            return True

        operand = ""
        #self.player.split()
        self.player.double_down()
        while operand != "Stand":
            bust = False
            operand = input("Hit or Stand? ")

            '' if operand == "Hit" or operand == "Stand" else print('Please try again!')

            if operand == "Hit":
                bust = self.player.hit()
                self.player.show()
                if self.player.check_black_jack():
                    print("Player got Blackjack! Congrats!")
                    return True
            if bust:
                print("Player busted. Good Game!")
                return True
        print("\n")
        self.dealer.show()
        if dealer_report:
            print("Dealer got Blackjack! Better luck next time!")
            return True

        while self.dealer.validate_score() < 18:
            if self.dealer.hit():
                self.dealer.show()
                print("Dealer busted. Congrats!")
                return True
            if self.player.check_black_jack():
                if self.player.check_black_jack():
                    self.dealer.show()
                    print("Dealer got Blackjack! Congrats!")
            self.dealer.show()

        if self.dealer.validate_score() == self.player.validate_score():
            print("It's a Tie. Better luck next time!")
        elif self.dealer.validate_score() > self.player.validate_score() and self.dealer.validate_score() <= 21:
            print("Dealer wins. Good Game!")
        elif self.dealer.validate_score() < self.player.validate_score() and self.player.validate_score() <= 21:
            print("Player wins. Congratulations!")


if __name__ == '__main__':
    b = Blackjack()
    b.play()
