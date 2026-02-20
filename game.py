import random
from card import Card


class Deck:
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

    def __init__(self):
        self.cards = []

        for rank in Deck.ranks:
            for suit in Deck.suits:
                self.cards.append(Card(rank, suit))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None


class Player:
    def __init__(self):
        self.money = 1000
        self.hand = []

    def get_hand(self):
        return self.hand

    def receive_card(self, card):
        self.hand.append(card)

    def print_hand(self):
        print("Current Hand: ", *self.hand)

    def clear_hand(self):
        self.hand = []

    def get_money(self):
        return self.money

    def set_money(self, newMoney):
        self.money = newMoney


class Dealer(Player):
    def print_hand(self, round_num=0):
        if round_num == 1:
            print("Dealer's Hand:", self.hand[1])
        else:
            print("Dealer's Hand:", *self.hand)


class Game:
    @staticmethod
    def calculate_hand(hand):
        hand_value = 0
        num_aces = 0

        for card in hand:
            if card.rank == "A":
                num_aces += 1
                hand_value += card.get_card_value()
            else:
                hand_value += card.get_card_value()

        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1

        return hand_value

    def handle_blackjack(self, player, dealer, deck, bet=50):
        dealer_hand_value = Game.handle_dealer(dealer.get_hand(), dealer, deck)

        if dealer_hand_value == 21:
            print("Push (Tie)!")
            player.set_money(player.get_money() + bet)
        else:
            print("BLACKJACK!!!")
            player.set_money(player.get_money() + bet * 2)

    def handle_dealer(self, hand, dealer, deck):
        dealer.print_hand()
        hand_value = Game.calculate_hand(hand)

        while hand_value < 17:
            dealer.receive_card(deck.deal())
            hand_value = Game.calculate_hand(hand)
            dealer.print_hand()

        return hand_value
