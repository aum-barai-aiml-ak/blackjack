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
    def __init__(self):
        self.money = 1000
        self.hand = []

    def getHand(self):
        return self.hand

    def receiveCard(self, card):
        self.hand.append(card)

    def printHand(self):
        print("Current Hand: ", *self.hand)

    def clearHand(self):
        self.hand = []

    def getMoney(self):
        return self.money

    def setMoney(self, newMoney):
        self.money = newMoney


class Dealer(Player):
    def printHand(self, round_num=0):
        if round_num == 1:
            print("Dealer's Hand:", self.hand[1])
        else:
            print("Dealer's Hand:", *self.hand)


class Game:

    def calculateHand(self, hand):
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

    def handleBlackjack(self, player, dealer, deck, bet=50):
        dealer_hand_value = Game.handleDealer(dealer.getHand(), dealer, deck)

        if dealer_hand_value == 21:
            print("Push (Tie)!")
            player.setMoney(player.getMoney() + bet)
        else:
            print("BLACKJACK!!!")
            player.setMoney(player.getMoney() + bet * 2)

    def handleDealer(self, hand, dealer, deck):
        dealer.printHand()
        hand_value = Game.calculateHand(hand)

        while hand_value < 17:
            dealer.receiveCard(deck.deal())
            hand_value = Game.calculateHand(hand)
            dealer.printHand()

        return hand_value
