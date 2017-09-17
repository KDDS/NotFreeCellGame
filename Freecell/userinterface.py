from notfreecell import NotFreeCell


thePlayerOne = NotFreeCell()
thePlayerOne.showBoard()

while not(thePlayerOne.boardOne.Foundation1.isFull() and thePlayerOne.boardOne.Foundation2.isFull() and thePlayerOne.boardOne.Foundation3.isFull() and thePlayerOne.boardOne.Foundation4.isFull()):
    print("Do the Move [From, LocationIndex1, To, LocationIndex2]. Available Places :- Cascade[C], Foundation{F], OpenCell[OC]")
    From, LocationIndex1, To, LocationIndex2 = input('Enter the values separated by Commas').split(',')
    thePlayerOne.boardOne.moveCard(From, int(LocationIndex1),To , int(LocationIndex2))
    thePlayerOne.showBoard()