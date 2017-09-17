from deckofcard import Deck
from cascades import Cascade
from thefoudationcode import foundation
from theopencells import cell
import pandas as pd

class Board:

    def __init__(self):

        desired_width = 320
        pd.set_option('display.width', desired_width)

        self.theDeck = Deck()
        self.shuffledCards = self.theDeck.shuffle()

        ############### Area : C ###############
        self.Cascade1 = Cascade(7)
        self.Cascade2 = Cascade(7)
        self.Cascade3 = Cascade(7)
        self.Cascade4 = Cascade(7)
        self.Cascade5 = Cascade(6)
        self.Cascade6 = Cascade(6)
        self.Cascade7 = Cascade(6)
        self.Cascade8 = Cascade(6)

        ############### Area : F ###############
        self.Foundation1 = foundation(13)
        self.Foundation2 = foundation(13)
        self.Foundation3 = foundation(13)
        self.Foundation4 = foundation(13)

        ############### Area : OC ##############
        self.OpenCell1 = cell(1)
        self.OpenCell2 = cell(1)
        self.OpenCell3 = cell(1)
        self.OpenCell4 = cell(1)

        ############### Area : SET ##############
        self.listOfCascades = [self.Cascade1,self.Cascade2,self.Cascade3,self.Cascade4,self.Cascade5,self.Cascade6,self.Cascade7,self.Cascade8]
        self.listOfFoundations = [self.Foundation1, self.Foundation2, self.Foundation3, self.Foundation4]
        self.listOfCells = [self.OpenCell1,self.OpenCell2,self.OpenCell3,self.OpenCell4]
        self.gameSet = [self.listOfCascades,self.listOfCells,self.listOfFoundations]
        self.response = None

    def serveCascades(self):
       # print (self.shuffledCards)
        for i in self.shuffledCards[0:7]:
            self.Cascade1.push(i)
        for i in self.shuffledCards[7:14]:
            self.Cascade2.push(i)
        for i in self.shuffledCards[14:21]:
            self.Cascade3.push(i)
        for i in self.shuffledCards[21:28]:
            self.Cascade4.push(i)
        for i in self.shuffledCards[28:34]:
            self.Cascade5.push(i)
        for i in self.shuffledCards[34:40]:
            self.Cascade6.push(i)
        for i in self.shuffledCards[40:46]:
            self.Cascade7.push(i)
        for i in self.shuffledCards[46:52]:
            self.Cascade8.push(i)

    def showcaseCascade(self):

        self.Cascade1_df = pd.DataFrame({'Cascade - 0': self.Cascade1.column})
        self.Cascade2_df = pd.DataFrame({'Cascade - 1': self.Cascade2.column})
        self.Cascade3_df = pd.DataFrame({'Cascade - 2': self.Cascade3.column})
        self.Cascade4_df = pd.DataFrame({'Cascade - 3': self.Cascade4.column})
        self.Cascade5_df = pd.DataFrame({'Cascade - 4': self.Cascade5.column})
        self.Cascade6_df = pd.DataFrame({'Cascade - 5': self.Cascade6.column})
        self.Cascade7_df = pd.DataFrame({'Cascade - 6': self.Cascade7.column})
        self.Cascade8_df = pd.DataFrame({'Cascade - 7': self.Cascade8.column})

        self.df_cascade = pd.concat([self.Cascade1_df,self.Cascade2_df,self.Cascade3_df,self.Cascade4_df,self.Cascade5_df,self.Cascade6_df,self.Cascade7_df,self.Cascade8_df], ignore_index=False, axis=1)
        return self.df_cascade

    def showcaseCell(self):
        self.OpenCell1_df = pd.DataFrame({'Cell - 0': self.OpenCell1.column})
        self.OpenCell2_df = pd.DataFrame({'Cell - 1': self.OpenCell2.column})
        self.OpenCell3_df = pd.DataFrame({'Cell - 2': self.OpenCell3.column})
        self.OpenCell4_df = pd.DataFrame({'Cell - 3': self.OpenCell4.column})

        self.df_Foundation = pd.concat([self.OpenCell1_df, self.OpenCell2_df, self.OpenCell3_df, self.OpenCell4_df ], ignore_index=False,axis=1)
        return self.df_Foundation

    def showcaseFoundation(self):
        self.Foundation1_df = pd.DataFrame({'Foundation - 0': self.Foundation1.column})
        self.Foundation2_df = pd.DataFrame({'Foundation - 1': self.Foundation2.column})
        self.Foundation3_df = pd.DataFrame({'Foundation - 2': self.Foundation3.column})
        self.Foundation4_df = pd.DataFrame({'Foundation - 3': self.Foundation4.column})

        self.df_Foundation = pd.concat([self.Foundation1_df, self.Foundation2_df, self.Foundation3_df, self.Foundation4_df ], ignore_index=False,axis=1)
        return self.df_Foundation

    def cardParser(self,item):
        self.color = item[0]
        self.suits = item [1]
        self.values = item [3]
        return self.color,self.suits,self.values

    def moveCard(self,fromArea,fromIndex,toArea,toIndex):
        self.flag = False
        # ------CHECK SOURCE AND SELECT THE ITEM TO MOVE--------#
        if fromArea == 'C':
            if not self.listOfCascades[fromIndex].isEmpty():
                self.item = self.listOfCascades[fromIndex].peek()
                self.flag = True
            else:
                self.flag = False
        elif fromArea == 'OC':
            if not self.listOfCells[fromIndex].isEmpty():
                self.item = self.listOfCells[fromIndex].peek()
                self.flag = True
            else:
                self.flag = False
        else:
            self.flag = False
            self.msg = 'Invalid Source'
        # ------CHECK DESTINATION AND PUSH THE ITEM TO MOVE--------#
        if self.flag is True:
            #------CASCADE--------#
            if toArea == 'C':
                if self.listOfCascades[toIndex].isEmpty():
                    self.listOfCascades[toIndex].push(self.item)
                else:
                    self.top = self.listOfCascades[toIndex].peek()
                    self.color1, self.suits1, self.values1 = self.cardParser(self.top)
                    self.color2, self.suits2, self.values2 = self.cardParser(self.item)
                    if self.color1 != self.color2 and self.values1 == (self.values2 +1):
                        self.listOfCascades[toIndex].push(self.item)
                        self.msg = "True : Pushed item into Cascade"
                        self.response = 0
                    else:
                        self.msg = "False : Could not push into Cascade"
                        self.response = -1
                        self.flag = False
                        # --------#
            #  ------FOUNDATION--------#
            elif toArea == 'F':
                if self.listOfFoundations[toIndex].isEmpty():
                    self.listOfFoundations[toIndex].push(self.item)
                else:
                    self.top = self.listOfFoundations[toIndex].peek()
                    self.color1, self.suits1, self.values1 = self.cardParser(self.top)
                    self.color2, self.suits2, self.values2 = self.cardParser(self.item)
                    if self.color1 == self.color2 and (self.values1+1) == self.values2 :
                        self.listOfFoundations[toIndex].push(self.item)
                        self.msg = "True : Pushed item into Foundation"
                        self.response = 0
                    else:
                        self.msg = "False : Could not push into Foundation"
                        self.response = -2
                        self.flag = False
                        # --------#
            # ------OPEN CELL--------#
            elif toArea == 'OC':
                if self.listOfCells[toIndex].isEmpty():
                    self.listOfCells[toIndex].push(self.item)
                else:
                    #self.top = self.listOfCells[toIndex].peek()
                    #self.color1, self.suits1, self.values1 = self.cardParser(self.top)
                    #self.color2, self.suits2, self.values2 = self.cardParser(self.item)
                    #if self.color1 == self.color2 and self.values1 < self.values2 and fromArea in ('OC','C'):
                     #  self.msg = "True : Pushed item into Open Cell"
                     #   self.response = 0
                    #else:
                    self.msg = "False : Could not push into Open Cell"
                    self.response = -3
                    self.flag = False
                        # --------#
            # ------WRONG DESTINATION--------#
            else:
                self.msg = "Invalid move 'TO'"
                self.response = -4
                self.flag = False
        # ------WRONG SOURCE--------#
        else:
            self.msg = "Invalid move 'FROM'"
            self.response = -5
            self.flag = False
        # ------IF PUSH IS SUCCESSFUL , DELETE FROM DESTINATION--------#
        if self.flag is True:
            if fromArea == 'C':
                self.listOfCascades[fromIndex].pop()
            elif fromArea == 'OC':
                self.listOfCells[fromIndex].pop()
            else:
                self.flag = False
                self.msg = "False : Could not delete from the source"
                self.response = -6
        else:
            pass
        return self.flag


    def autoMove(self):

        # check the Ace in cascades
        self.counterCascade = -1
        self.listTrueAce = []
        for i in self.listOfCascades:
            self.counterCascade = self.counterCascade +1
            self.col, self.sut, self.val = self.cardParser(i.peek())
            if self.val == 1:
                self.listTrueAce =  self.listTrueAce + [self.counterCascade]
            else :
                pass

        # check the available foundations and inser
        self.counterFoundation = -1
        for i in self.listTrueAce:
            self.counterFoundation = self.counterFoundation + 1
            for j in self.listOfFoundations:
                if j.isEmpty():
                    self.moveCard('C',i,'F',self.counterFoundation)

# code to dynamically build cascades

"""def makecascade():
    allCascades = []
    cascadedColumns = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']
    counter = 0
    for i in cascadedColumns:
        counter = counter + 1
        if counter < 5:
            dynamicCode = "Cascade" + i + " = Cascade(7)"
            print(dynamicCode)
            allCascades = allCascades + [dynamicCode]  # the objects are created locally

        else:
            dynamicCode = "Cascade" + i + " = Cascade(6)"
            print(dynamicCode)
            allCascades = allCascades + [dynamicCode] # the objects are created locally
    return allCascades # globally available

listOfCascades = makecascade()
print(listOfCascades)
#exec(listOfCascades[1])
map(exec(),listOfCascades)
print('Hi')"""

# code to manually build cascades
# Need improvement ... BAD CODE

