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
        self.hands = [[]]

    def get_hand(self, index=0):
        return self.hands[index]

    def receive_card(self, card, index=0):
        self.hands[index].append(card)

    def add_hand(self, new_hand):
        self.hands.append(new_hand)

    def print_hand(self, index=0):
        print(f"Hand {index + 1}: ", *self.hands[index])

    def clear_hands(self):
        self.hands = [[]]

    def get_money(self):
        return self.money

    def set_money(self, newMoney):
        self.money = newMoney


class Dealer(Player):
    def print_hand(self, round_num=0):
        current_hand = self.get_hand(0) 
        if round_num == 1:
            print("Dealer's Hand: [Hidden],", current_hand[1])
        else:
            print("Dealer's Hand:", *current_hand)



class Game:
    def __init__(self, player, dealer, deck, bet=50):
        self.player = player
        self.dealer = dealer
        self.deck = deck
        self.bet = bet

    def can_split(self, hand):
        # Standard Rule: Can split if cards have the same VALUE (e.g., King and Jack)
        return len(hand) == 2 and hand[0].get_card_value() == hand[1].get_card_value()

    def split_hand(self, hand_index):
        if hand_index >= len(self.player.hands):
            return False
            
        current_hand = self.player.hands[hand_index]

        if not self.can_split(current_hand):
            print("Cannot split this hand.")
            return False

        # 1. Deduct additional bet
        if self.player.get_money() < self.bet:
            print("Not enough money to split.")
            return False
            
        self.player.set_money(self.player.get_money() - self.bet)

        # 2. Separate the cards
        split_card = current_hand.pop()
        new_hand = [split_card]

        # 3. Add the new hand to the player's list
        self.player.add_hand(new_hand)

        # 4. Deal a new card to both hands
        current_hand.append(self.deck.deal())
        new_hand.append(self.deck.deal())
        
        print("Hand split successfully!")
        return True

    @staticmethod
    def calculate_hand(hand):
        hand_value = 0
        num_aces = 0

        for card in hand:
            if card.rank == "A":
                num_aces += 1
                hand_value += 11 
            else:
                hand_value += card.get_card_value()

        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1

        return hand_value

    def handle_dealer(self):
        self.dealer.print_hand(round_num=2) 
        hand_value = self.calculate_hand(self.dealer.get_hand(0))

        while hand_value < 17:
            print("Dealer hits...")
            card = self.deck.deal()
            if card:
                self.dealer.receive_card(card, index=0)
                hand_value = self.calculate_hand(self.dealer.get_hand(0))
                self.dealer.print_hand(round_num=2)
            else:
                break
        
        print(f"Dealer stands at {hand_value}")
        return hand_value

    def determine_winner(self):
        # We must iterate through all player hands (in case of split)
        dealer_value = self.handle_dealer()
        
        for i, hand in enumerate(self.player.hands):
            player_value = self.calculate_hand(hand)
            print(f"--- Result for Hand {i+1} ---")
            
            if player_value > 21:
                print(f"Hand {i+1} Busted! You lose.")
                # Money already lost (bet not returned)
            elif dealer_value > 21:
                print(f"Dealer Busted! Hand {i+1} wins.")
                self.player.set_money(self.player.get_money() + (self.bet * 2))
            elif player_value > dealer_value:
                print(f"Hand {i+1} wins ({player_value} vs {dealer_value}).")
                self.player.set_money(self.player.get_money() + (self.bet * 2))
            elif player_value == dealer_value:
                print(f"Push (Tie) at {player_value}.")
                self.player.set_money(self.player.get_money() + self.bet)
            else:
                print(f"Dealer wins ({dealer_value} vs {player_value}).")