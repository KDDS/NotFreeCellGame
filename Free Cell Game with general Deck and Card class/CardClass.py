class Card:

    def __init__(self):
        # Contains the card attributes
        # defines the faces of the cards
        self.cardFace = ['Jack', 'Queen', 'King']
        # defines the suits of the cards
        self.ColorMap = {'Black': ['Clubs', 'Spade'], 'Red': ['Heart', 'Diamond']}
        self.CardSuits = list(self.ColorMap.values())
        self.CardColor = list(self.ColorMap.keys())

    def enhanceCard(self, listed):
        """ Enhances the card by adding color and providing Face Values. Returns a modified list """

        card = listed
        counter1d = -1

        # fetched the color and the suit of the card in test
        color, suit = self.parseSuitIndex(card[0])
        # Adds suit name to the card
        card.insert(0, suit)
        # Adds suit color to the card
        card.insert(1, color)
        # Removes the suit index
        del card[2]
        currentCard = card
        # Replaces 1 with ACE
        for array in card:
            if array == 1:
                currentCard[2] = 'Ace'

        return currentCard

    def parseSuitIndex(self, values):
        """ Parses the suit name and color from the dictionary values"""

        listOfSuit = []
        counter = -1
        # Fetch the name of the suit from the index
        lengthOfArray = len(self.CardSuits)
        for i in range(lengthOfArray):
            value = i
            for item in self.CardSuits[i]:
                listOfSuit = listOfSuit + [item]
        suitToCheck = listOfSuit[values]

        # Fetch the name of the color for the suit
        for i in range(lengthOfArray):
            if suitToCheck in self.CardSuits[i] or counter > 1:
                counter = i
            else:
                pass
        colorToFind = self.CardColor[counter]

        return suitToCheck, colorToFind


    def getCardFace(self):
        """ Mutator to the fetch all the faces available in the card attribute."""

        return self.cardFace

    def __str__(self):
        """ Describes the Card Class for any instance. """

        return '\nThe card details are :\n>Face: {0} \n>Suits: {1}\n '.format(self.getCardFace(), self.CardSuits)


def main():
    pass
if __name__ == "__main__":
    main()