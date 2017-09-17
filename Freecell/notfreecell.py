from gameboard import Board


class NotFreeCell:

    def __init__(self):

        self.boardOne = Board()
        self.boardOne.serveCascades()

    def showBoard(self):

        self.boardOne.autoMove()
        print('.' * 145)
        print('.' +'\t' * 15 + 'FOUNDATIONS [F]' +'\t' * 18 +'.')
        print('.' * 145+ '\n')
        print(self.boardOne.showcaseFoundation())
        print('\n')
        print('.' * 145)
        print('.' +'\t' * 15 + 'OPEN CELLS [OC]' +'\t' * 18 +'.')
        print('.' * 145+ '\n')
        print(self.boardOne.showcaseCell())
        print('\n')
        print('.' * 225)
        print('.' +'\t' * 25 + 'CASCADES [C]' +'\t' * 28 +'.')
        print('.' * 225+ '\n')
        print(self.boardOne.showcaseCascade())
        print('.' * 225)

"""thePlayerOne = NotFreeCell()
thePlayerOne.showBoard()

while not (thePlayerOne.boardOne.Foundation1.isFull() and thePlayerOne.boardOne.Foundation2.isFull() and thePlayerOne.boardOne.Foundation3.isFull() and thePlayerOne.boardOne.Foundation4.isFull()):
    print("Do the Move [From, LocationIndex1, To, LocationIndex2]. Available Places :- Cascade[C], Foundation{F], OpenCell[OC]")
    From, LocationIndex1, To, LocationIndex2 = input('Enter the values separated by Commas').split(',')
    thePlayerOne.boardOne.moveCard(From, int(LocationIndex1), To, int(LocationIndex2))
    thePlayerOne.showBoard()"""







            #thePlayerOne = NotFreeCell()
#thePlayerOne.showBoard()