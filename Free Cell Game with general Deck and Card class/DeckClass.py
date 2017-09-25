from CardClass import Card
import random as rnd


class Deck:

    def __init__(self, value_start, value_end, number_of_suits):
        # Object of Card to use them in this instance of Deck.
        self.theCard = Card()
        # Initial value of the suit of a card
        self.startIndex = value_start
        # Final value of the suit of a card
        self.endIndex = value_end
        # Number of available suits in the card
        self.variety = number_of_suits
        # Available series for the card
        self.currentList = []
        # Contains the list of cards available to prepare the deck
        self.currentSuitedList = []
        # Refers the Deck with shuffled cards. May be accessed from different class
        self.currentSuitedListShuffled = []
        # Puts a drawn card from the deck using method : drawTheCard
        self.drawnCard = None

    def addToDeck(self):
        """ Create the deck required for the game play. Returns a list of range x Suit number of cards where
        each card is represented by suit index and a value index"""

        templist = []
        LenofFaces = + len(self.theCard.getCardFace())
        # Generate the list of values when the requested card range is 10
        if self.endIndex <= 10:
            templist = [numbers for numbers in range(self.startIndex, self.endIndex+1)]
        # Generate the list of values when the requested card range is between 10 and 10+(number of faces)
        elif 10 < self.endIndex <= (10+LenofFaces):
            templist = [numbers for numbers in range(self.startIndex, 11)] + self.theCard.getCardFace()[:self.endIndex % 10]
        # Generate the list of values when the requested card range is greater than 10
        else:
            templist = [numbers for numbers in range(self.startIndex, self.endIndex - LenofFaces + 1)] + self.theCard.getCardFace()
        # Pass the above range to internally build the series of cards
        print('Series with Face:' , templist)
        self.currentSuitedList = self.moduloDeck(templist)
        #return templist

    def moduloDeck(self, theRange):
        """ This function is the algorithm to generate the real number of cards from the given range in deck
        constructor. Returns a modified list """

        theModList = []
        # Creates the suits for the number of varieties required for the deck
        for suits in range(0, self.variety):
            for values in theRange:
                tempList = [suits,values]
                # Create the list which contains different condition of suits and values in arrays
                theModList.append(tempList)
        # Enhance the built list for user readability and better implementation
        enhancedList = theModList
        return enhancedList

    def shuffle(self):
        """ Shuffles the generated deck """
        self.currentSuitedListShuffled = self.currentSuitedList.copy()
        rnd.shuffle(self.getCurrentSuitedListShuffled())
        return self.getCurrentSuitedListShuffled()

    def drawTheCard(self):
        """ Draw a card from the shuffled Deck """

        self.drawnCard = self.theCard.enhanceCard(self.getCurrentSuitedListShuffled().pop())
        return self.drawnCard

    def getCurrentSuitedListShuffled (self):
        """ Mutator to the fetch the shuffled list of cards """

        return self.currentSuitedListShuffled

    def __str__(self):
        """ Describes the Deck Class for the instance. """

        return '\nThe cards generated are [total = {0}]: \n{1}\n\nThe shuffled Deck generated is: \n{2}\n'\
            .format(len(self.currentSuitedList), self.currentSuitedList, self.getCurrentSuitedListShuffled())


def main():
    pass
if __name__ == "__main__":
    main()

