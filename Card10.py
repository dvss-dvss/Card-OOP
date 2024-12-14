from import_card import Card
from import_Unprintable_Card import Unprintable_Card
from import_Positionable_Card import Positionable_Card
from import_hand import Hand
from import_deck import Deck

#main
card1 = Card("Т", Card.SUITS[0])
card2 = Unprintable_Card("Т", Card.SUITS[1])
card3 = Positionable_Card("Т", Card.SUITS[2])
print("Друкую об'ект Card:")
print(card1)
print("Друкую об'ект Unprintable_Card:")
print(card2)
print("Друкую об'ект Positionable_Card:")
print(card3)
print("Перевертаю об'ект Positionable_Card.")
card3.flip()
print("Друкую об'ект Positionable_Card:")
print(card3)