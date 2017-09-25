from GameClass import NotFreecell


class Player:

    def interface(self):

        modifier = 'C'
        text = ''

        # Splits the cards into eight cascades
        name = input('Enter player name')
        thePlayerOne = NotFreecell(name)
        print(thePlayerOne)
        thePlayerOne.fillCascades()
        thePlayerOne.showBoard()

        # Game is played until its finished
        while not (len(thePlayerOne.listOfFoundations[0]) == 13 and
                           len(thePlayerOne.listOfFoundations[1]) == 13 and
                           len(thePlayerOne.listOfFoundations[2]) == 13 and
                           len(thePlayerOne.listOfFoundations[3]) == 13):

            modifier = input('Type Q to quit or C to Continue or R to Restart').upper()

            # Quit the game
            if modifier == 'Q':
                text = 'Thanks for playing'
                break
            # Restart the game
            elif modifier == 'R':
                self.interface()
                break
            # Continue the game
            elif modifier == 'C':
                text = 'Thanks for playing'
                pass
            # Invalid Input
            else:
                text = 'Invalid choice, Quitting the game'
                break

            print("Place your Card [From, LocationIndex1, To, LocationIndex2]. Available Places :-"
                  " Cascade[C], Foundation{F],"" OpenCell[OC]")

            From, LocationIndex1, To, LocationIndex2 = input('Enter the values separated by Commas').upper().split(',')

            error, response = thePlayerOne.moveCard(From, int(LocationIndex1), To, int(LocationIndex2))
            if error is True:
                thePlayerOne.autoMove()
                thePlayerOne.showBoard()

            print(thePlayerOne.listOfCells)
            print(response, '-', error)

        #if modifier in ['Q', 'C']:
        print(text)


def main():
    # Start the game
    gameInstance = Player()
    gameInstance.interface()
if __name__ == "__main__":
    main()