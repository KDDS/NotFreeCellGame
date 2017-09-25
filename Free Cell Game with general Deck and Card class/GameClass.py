from DeckClass import Deck
import pandas as pd


class NotFreecell:

    def __init__(self, name):
        # Set the dimension of the data frame to display the game in a page without word wraps
        desired_width = 320
        pd.set_option('display.width', desired_width)

        # Initialize the object of Deck for further use
        self.theDeck = Deck(1, 13, 4)
        # Add the cards to the decks
        self.theDeck.addToDeck()
        # Shuffle the deck
        self.theDeck.shuffle()

        # Initializing rhe game components viz: CASCADES, FOUNDATIONS and OPENCELLS
        self.listOfCascades = [[], [], [], [], [], [], [], []]
        self.listOfFoundations = [[], [], [], []]
        self.listOfCells = [[], [], [], []]

        # Instance variables
        self.peekedValue = None
        self.color = None
        self.suits = None
        self.values = None
        self.item = None

        # Game response when an move is made by the user
        self.flag = True
        self.msg = None

        # Visualisation
        self.df_cascade = None
        self.df_Foundation = None
        self.df_OpenCell = None

        #Player details
        self.name = name


    def fillCascades(self):
        """ Splits the deck of cards into eight cascades. First four of the cascade contain seven cards each and the
        other four cascades contain six cards each"""

        for cascades in self.listOfCascades:
                # put the values in the first four cascades where the number of cards is 7 for each
                if self.listOfCascades.index(cascades) < 4:
                    limits = 7
                    for terms in range(0, limits):
                        cascades.append(self.theDeck.drawTheCard())
                else:
                    # put the values in the last four cascades where the number of cards is 6 for each
                    limits = 6
                    for terms in range(0, limits):#
                        cascades.append(self.theDeck.drawTheCard())

    def cardParser (self, arrayedComponent):
        """ Parse the array to determine the value of the card. Returns the Color, Suit and Value of the input card """

        self.color = arrayedComponent[0]
        self.suits = arrayedComponent[1]

        if arrayedComponent[2] == 'Jack':
            self.values = 11
        elif arrayedComponent[2] == 'Queen':
            self.values = 12
        elif arrayedComponent[2] == 'King':
            self.values = 13
        elif arrayedComponent[2] == 'Ace':
            self.values = 1
        else:
            self.values = arrayedComponent[2]

        return self.color, self.suits, self.values

    def moveCard(self, fromArea, fromIndex, toArea, toIndex):
        """ Moves the card between various location in the game """

        ################################################
        #  Check the SOURCE and select the item to move#
        ################################################

        self.flag = False
        # First, it checks if the source is Cascade
        if fromArea == 'C':

            if self.listOfCascades[fromIndex]:
                self.item = self.listOfCascades[fromIndex][-1]
                self.flag = True
            else:
                # If thr Cascade is empty
                self.msg = 'Selected Cascade is Empty'
                self.flag = False

        # Second, it checks if the source is OpenCell
        elif fromArea == 'OC':

            if self.listOfCells[fromIndex]:
                self.item = self.listOfCells[fromIndex][-1]
                self.flag = True
            else:
                # If thr OpenCell is empty
                self.msg = 'Selected Open Cell is Empty'
                self.flag = False

        # Thirdly, it checks if the source is Foundation
        elif fromArea == 'F':

            if self.listOfFoundations[fromIndex]:
                self.item = self.listOfFoundations[fromIndex][-1]
                self.flag = True
            else:
                # If the Foundation is empty
                self.msg = 'Selected Foundation is Empty'
                self.flag = False

        # Fourthly, if the source is invalid
        else:
            self.flag = False
            self.msg = 'Selected Source is Invalid. Available Source : C, OC, F'

        ######################################################
        #  Check the DESTINATION and push the selected item  #
        ######################################################

        if self.flag is True:
            # Checks if the destination is Cascade
            if toArea == 'C':

                # if empty then push the selected item
                if not self.listOfCascades[toIndex]:
                    self.listOfCascades[toIndex].append(self.item)
                else:
                    # If not empty, compare the selected item with the last card in the cascade
                    self.top = self.listOfCascades[toIndex][-1]
                    self.color1, self.suits1, self.values1 = self.cardParser(self.top)
                    self.color2, self.suits2, self.values2 = self.cardParser(self.item)

                    """ push the item if the rule matches, i.e the selected item is of different color than the 
                        last card in the cascade. It also satisfies that the value of the selected card is lesser
                        than the last card in the cascade"""

                    if self.color1 != self.color2 and self.values1 == (self.values2 +1):
                        self.listOfCascades[toIndex].append(self.item)
                        self.msg = "Pushed item into Cascade"
                    else:
                        self.msg = "Invalid move to Cascade"
                        self.flag = False

            # Checks if the destination is Foundation
            elif toArea == 'F':

                # if empty then push the selected item into the Foundation
                if not self.listOfFoundations[toIndex]:
                    self.color3, self.suits3, self.values3 = self.cardParser(self.item)
                    if self.values3 == 1:
                        self.listOfFoundations[toIndex].append(self.item)
                    else:
                        self.msg = "Invalid move to Foundation"
                        self.flag = False
                else:
                    # If not empty, compare the selected item with the last card in the Foundation
                    self.top = self.listOfFoundations[toIndex][-1]
                    self.color1, self.suits1, self.values1 = self.cardParser(self.top)
                    self.color2, self.suits2, self.values2 = self.cardParser(self.item)

                    """ push the item if the rule matches, i.e the selected item is of different color than the 
                        last card in the cascade. It also satisfies that the value of the selected card is lesser
                        than the last card in the cascade"""

                    if self.suits1 == self.suits2 and (self.values1+1) == self.values2:
                        self.listOfFoundations[toIndex].append(self.item)
                        self.msg = "Pushed item into Foundation"
                    else:
                        self.msg = "Invalid move to Foundation"
                        self.flag = False

            # Checks if the destination is OpenCell
            elif toArea == 'OC':

                # If empty then push the selected item into the OpenCell
                if not self.listOfCells[toIndex]:
                    self.listOfCells[toIndex].append(self.item)
                    self.msg = "Pushed item into OpenCell"
                else:
                    # Do not push into a full OpenCell
                    self.msg = "Invalid move to OpenCell"
                    self.flag = False

            # Checks if the destination is invalid
            else:
                self.msg = "Invalid move(To).  Available destinations : C, OC, F'"
                self.flag = False
        else:
            pass

        ######################################################
        #  Check the DESTINATION and push the selected item  #
        ######################################################

        # If the push is successful then remove the item from the source
        if self.flag is True:
            if fromArea == 'C':
                self.listOfCascades[fromIndex].pop()
            elif fromArea == 'OC':
                self.listOfCells[fromIndex].pop()
            else:
                self.flag = False
                self.msg = "Cannot remove from the Source"
        else:
            pass
        return self.flag, self.msg

    def autoMove(self):
        """ Determines if there is any ACE value in the last item of the cascades. If present, move it to the open
            Foundation"""

        # check the Ace in cascades
        counterCascade = -1
        listTrueAce = []
        for i in self.listOfCascades:
            counterCascade = counterCascade + 1
            # parses the value of the last card in the cascades and validates i
            self.color, self.suits, self.values = self.cardParser(i[-1])
            if self.values == 1:
                listTrueAce = listTrueAce + [counterCascade]
            else:
                pass

        # check the available foundations and insert the Ace from the cascade
        self.counterFoundation = -1
        for i in listTrueAce:
            self.counterFoundation = self.counterFoundation + 1
            for j in self.listOfFoundations:
                if not j:
                    self.moveCard('C', i, 'F', self.counterFoundation)

    def showcaseCascade(self):
        """ Concatenates all the cascades and returns a DataFrame """

        # Convert the list of cascades into eight DataFrame
        Cascade1_df = pd.DataFrame({'Cascade - 0': self.listOfCascades[0]})
        Cascade2_df = pd.DataFrame({'Cascade - 1': self.listOfCascades[1]})
        Cascade3_df = pd.DataFrame({'Cascade - 2': self.listOfCascades[2]})
        Cascade4_df = pd.DataFrame({'Cascade - 3': self.listOfCascades[3]})
        Cascade5_df = pd.DataFrame({'Cascade - 4': self.listOfCascades[4]})
        Cascade6_df = pd.DataFrame({'Cascade - 5': self.listOfCascades[5]})
        Cascade7_df = pd.DataFrame({'Cascade - 6': self.listOfCascades[6]})
        Cascade8_df = pd.DataFrame({'Cascade - 7': self.listOfCascades[7]})

        # ignore_index = false, axis = 1 allows to concatenate dataframe of different length without renaming columns
        self.df_cascade = pd.concat([Cascade1_df, Cascade2_df, Cascade3_df, Cascade4_df,
                                    Cascade5_df, Cascade6_df, Cascade7_df, Cascade8_df],
                                    ignore_index=False, axis=1)

        # Sets the NAN value of the DataFrame to '[EMPTY]'
        self.df_cascade = self.df_cascade.fillna('[EMPTY]')

        return self.df_cascade

    def showcaseCell(self):
        """ Concatenates all the Foundations and returns a DataFrame """

        # Convert the list of cascades into eight DataFrame
        OpenCell1_df = pd.DataFrame({'Cell - 0': self.listOfCells[0]})
        OpenCell2_df = pd.DataFrame({'Cell - 1': self.listOfCells[1]})
        OpenCell3_df = pd.DataFrame({'Cell - 2': self.listOfCells[2]})
        OpenCell4_df = pd.DataFrame({'Cell - 3': self.listOfCells[3]})

        # ignore_index = false, axis = 1 allows to concatenate dataframe of different length without renaming columns
        self.df_OpenCell = pd.concat([OpenCell1_df, OpenCell2_df, OpenCell3_df, OpenCell4_df],
                                ignore_index=False, axis=1)

        # Sets the NAN value of the DataFrame to '[EMPTY]'
        self.df_OpenCell = self.df_OpenCell.fillna('[EMPTY]')

        return self.df_OpenCell

    def showcaseFoundation(self):
        """ Concatenates all the Foundations and returns a DataFrame """

        # Convert the list of foundations into eight DataFrame
        Foundation1_df = pd.DataFrame({'Foundation - 0': self.listOfFoundations[0]})
        Foundation2_df = pd.DataFrame({'Foundation - 1': self.listOfFoundations[1]})
        Foundation3_df = pd.DataFrame({'Foundation - 2': self.listOfFoundations[2]})
        Foundation4_df = pd.DataFrame({'Foundation - 3': self.listOfFoundations[3]})

        # ignore_index = false, axis = 1 allows to concatenate dataframe of different length without renaming columns
        self.df_Foundation = pd.concat([Foundation1_df, Foundation2_df, Foundation3_df,
                                        Foundation4_df], ignore_index=False, axis=1)

        # Sets the NAN value of the DataFrame to '[EMPTY]'
        self.df_Foundation = self.df_Foundation.fillna('[EMPTY]')

        return self.df_Foundation

    def showBoard(self):
        """ Displays the cards in the game"""

        # Before every display it automatically moves the Ace from the Cascades to the Foundation
        # Build the foundation display
        print('.' * 145)
        print('.' + '\t' * 15 + 'FOUNDATIONS [F]' + '\t' * 18 + '.')
        print('.' * 145 + '\n')
        print(self.showcaseFoundation())
        print('\n')

        # Build the OpenCell display
        print('.' * 145)
        print('.' + '\t' * 15 + 'OPEN CELLS [OC]' + '\t' * 18 + '.')
        print('.' * 145 + '\n')
        print(self.showcaseCell())
        print('\n')

        # Build the Cascade display
        print('.' * 193)
        print('.' + '\t' * 20 + 'CASCADES [C]' + '\t' * 25 + '.')
        print('.' * 193 + '\n')
        print(self.showcaseCascade())
        print('\n')
        print('.' * 193)
        print('.' + '\t' * 48 + '.')
        print('.' * 193)

    def __str__(self):
        """ prints the name of the player """

        line_0 = ' \n'
        line_1 = ('.' * 145 + '\n')
        line_2 = ('.' + '\t' * 13 + 'Welcome to Not Free Cell game' + '\t' * 16 + '.'+'\n')
        line_3 = ('.' * 145 + '\n\n')
        line_4 = ('Player Name: ' + self.name + '\n')
        return line_0+line_1+line_2+line_3+line_4


def main():
    pass
if __name__ == "__main__":
    main()