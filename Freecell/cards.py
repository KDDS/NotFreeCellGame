import random as rnd

class Card:

    def __init__(self, Color, Suit):

        # Define the card values
        self.cardValues = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                           9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
        # Copy the values
        self.currentValues = self.cardValues.copy()
        # Define the suit of the card
        self.cardSuits = Suit
        # Define the color of the card
        self.cardColor = Color
        # Define the deck of each suit for 13 cards
        self.decked = None
        # Define each card along with suit and color
        self.suitCard = None
        # Randomize the 13 cards of the suit
        self.shuffledCard = []

    def deckOfSuite(self):
        """Defines the deck of each suit of cards.
           Returns 13 cards of each set"""
        self.decked = [self.cardSuits, self.cardColor, self.currentValues]
        return (self.decked)

    def draw(self):
        """Draws each card from the deckOfSuite()"""
        assert not self.deckWeight() == 0, "suit deck is empty"
        indexed = rnd.choice([i for i in self.currentValues.keys()])
        self.suitCard = [self.cardColor,self.cardSuits,self.currentValues[indexed],indexed]
        self.shuffledCard = self.shuffledCard + []
        del self.currentValues[indexed]
        return self.suitCard

    def deckWeight(self):
        length = len (self.currentValues)
        return length

    def isEmpty(self):
        if self.deckWeight() == 0:
             self.Flag = True
        else:
             self.Flag = False
        return self.Flag

