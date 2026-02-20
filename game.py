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
        Deck.shuffle(self)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None


class Player:
    pass


class Dealer(Player):
    pass
