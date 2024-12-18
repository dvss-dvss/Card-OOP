class Card:
    """Гральна карта."""
    RANKS = ["Т", "2", "3", "5", "6", "7",
             "8", "9", "10", "В", "Д", "К"]
    
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep
    
class Hand:
    """Рука: набір карт на руках одного гравця."""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep+= str(card) + "\t"
        else:
            rep = "<пусто>"
        return rep
    
    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

card1 = Card(rank="Т", suit = Card.SUITS[0])
print("Виводжу на екран об'экт-карту:")
print(card1)

card2 = Card(rank="2", suit = Card.SUITS[0])
card3 = Card(rank="3", suit = Card.SUITS[0])
card4 = Card(rank="4", suit = Card.SUITS[0])
card5 = Card(rank="5", suit = Card.SUITS[0])
print("\nВиводжу ще чотири карти:")
print(card2)
print(card3)
print(card4)
print(card5)