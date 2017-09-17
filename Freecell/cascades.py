class Cascade:

    error_code = 1

    def __init__(self,length):
        self.column = []        # represent the stack as a list
        self.size  = length     # represent the maximum size o the stack
        self.currSize = 0       # indicate the current size of the stack
        self.currTop = -1       # indicate the top position of the stack
        self.cardAttributes = None


    # returns the number of items in the stack
    def __len__(self):
        return self.currSize

    # returns True if the stack is empty or False otherwise
    def isEmpty(self):
        return len(self)==0

    # pushes an item onto the top of the stack
    def push(self,item):
        assert not self.isFull(), "Cannot push into a full stack"
        self.column.append(item)
        self.currSize = self.currSize + 1
        self.currTop = self.currTop + 1

    # pushes an item onto the top of the stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        item = self.column[self.currTop]
        self.currSize = self.currSize - 1
        self.currTop = self.currTop - 1
        del self.column[len(self)]
        return item

    # returns True if the stack is full or False otherwise
    def isFull (self):
        return len(self) == self.size

    # returns the item on the stack without removing it
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        cardPeek = self.column[self.currTop]
        return cardPeek

    # returns the entire stack
    def showAll(self):
        return self.column


