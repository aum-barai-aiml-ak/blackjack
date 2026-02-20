class Card:
    VALUES = {
        "A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = Card.VALUES[rank]

    def __repr__(self):
        return f"{self.rank} of {self.suit} (Value: {self.value})"

    def get_card_value(self):
        return self.value
