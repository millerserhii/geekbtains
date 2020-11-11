from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def suit_cons(self):
        pass

    @abstractmethod
    def coat_cons(self):
        pass


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def suit_cons(self):
        return round(self.h * 2 + 0.3, 2)

    def coat_cons(self):
        return "this is no coat"


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def coat_cons(self):
        return round(self.v/6.5 + 0.5, 2)

    def suit_cons(self):
        return "this is not suit"


suit1 = Suit(10)
print(suit1.suit_cons)
coat1 = Coat(15)
print(coat1.coat_cons)
