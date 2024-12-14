from import_card import Card
class Unprintable_Card(Card):
    """карта, номинал та масть якои
    не можуть бути виведени на екран."""

    def __str__(self):
        return "<не можна надрукувати>"