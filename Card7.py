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
print("Виводжу на екран об'єкт-карту:")
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

my_hand = Hand()
print("\nДрукую карти, які у мене на руках до роздачи:")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nДрукую п'ять карт, які з'явилися у мене на руках:")
print(my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nПреші дві з моїх карт я передав вам.")
print("Тепер у вас на руках:")
print(your_hand)
print("А у мене на руках:")
print(my_hand)

my_hand.clear()
print("\nА у мене на руках після того, як я скинув усі карти:")
print(my_hand)