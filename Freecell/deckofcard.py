import random as rnd
from cards import Card

class Deck:
    Clubs = Card('Black', 'Clubs')
    def __init__(self):
        self.Clubs = Card('Black', 'Clubs')
        self.Spades = Card('Black', 'Spades')
        self.Diamonds = Card('Red', 'Diamonds')
        self.Hearts = Card('Red', 'Hearts')
        self.suiteList = [self.Clubs,self.Spades,self.Diamonds,self.Hearts]
        self.Decked =[]

    def shuffle(self):
        while len(self.Decked) < 52:
            indexed = rnd.randint(0, 3)
            if self.suiteList[indexed].isEmpty() is False:
                self.Decked = self.Decked + [self.suiteList[indexed].draw()]
            else:
                self.Decked = self.Decked
        return self.Decked

