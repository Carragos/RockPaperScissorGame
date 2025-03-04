from HandGestures import Rock, Paper, Scissors, HandGestures
import random
import sys

class Player():
    def __init__(self):
        self.currentScore = 0
        self.currentDraw: HandGestures | None = None
        self.handGestureList = [Rock, Paper, Scissors]
        rock, paper, scissor = Rock(), Paper(), Scissors()
        self.handGestureList = [rock, paper, scissor]

    def stringCurrentDraw(self):
        return str(self.currentDraw)
    
    def scorePoint(self):
        self.currentScore += 1

    def setCurrentDraw(self, newDraw):
        self.currentDraw = newDraw

    def returnGestureTypeFromList(self, string):
        if string in ['r', 'p', 's']:
            match string:
                case 'r':
                    return self.handGestureList[0]
                case 'p':
                    return self.handGestureList[1]
                case 's':
                    return self.handGestureList[2]
                case _:
                    print("Something went wrong...")
                    sys.exit()

class ComputerPlayer(Player):

    def returnRandomDraw(self):
        return random.choice(self.handGestureList)
    
    def makeRandomDraw(self):
        self.currentDraw = self.returnRandomDraw()

class HumanPlayer(Player):
    def makeChoice(self):
        print('\n')
        print("Rock, Paper or Scissors (r/p/s)")

        userChoice = input().strip()
        while userChoice not in ['r', 'p', 's']:
            print("Please provide a vaild input. (r/p/s)")
            userChoice = input().strip()
        self.currentDraw = self.returnGestureTypeFromList(userChoice)