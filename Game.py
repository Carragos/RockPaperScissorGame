
from Players import HumanPlayer, ComputerPlayer

class Game:    
    def __init__(self):
        self.humanPlayer = HumanPlayer()
        self.computerPlayer = ComputerPlayer()
        self.gameRounds = 0 # Default starting rounds
        self.roundCounter = 0
        self.drawCounter = 0

    def startGame(self):
        print('--- Rock Paper Scissors Game ---')
        print('--- How many rounds would you like to play?')

        userInput = input()

        while (not userInput.isdigit()):
            print('\nPlease enter a valid digit.')
            userInput = input()
        
        try:
            intUserInput = int(userInput)
        except:
            print("Conversion to intiger failed")
            print('Restarting game...')

            self.startGame()

        self.gameRounds = intUserInput

        print(f"Okay, we are going to play {self.gameRounds} rounds!")

    def printDrawingResults(self):
        print('You: ' + str(self.humanPlayer.currentDraw) + '\nComputer: ' + str(self.computerPlayer.currentDraw))

    def printCurrentScoreTable(self):
            print('Round ' + str(self.roundCounter) + ' results: ')
            print('You: ' + str(self.humanPlayer.currentScore) + ' | Computer: ' + str(self.computerPlayer.currentScore) + ' | Draws: ' + str(self.drawCounter))

    def playRound(self):
        self.roundCounter += 1
        self.humanPlayer.makeChoice()
        self.computerPlayer.makeRandomDraw()

        print('\n')
        self.printDrawingResults()

        beatResult = self.humanPlayer.currentDraw.returnCheckBeat(self.computerPlayer.currentDraw)

        match beatResult:
            case -1: # Computer gets point
                print('LOST! The computer scored a point')
                self.computerPlayer.scorePoint()
            case 0: # Draw, rerun round
                print('DRAW! Noone gets a point...')
                self.drawCounter += 1
            case 1: # Won, Human gets point
                print('WON! You scored a point')
                self.humanPlayer.scorePoint()
            case _:
                print('Something went wrong...')

        self.printCurrentScoreTable()

    def finalScoreAnalysis(self):
        if self.humanPlayer.currentScore > self.computerPlayer.currentScore:
            print('Congratulatuions! You won the game!')
        elif self.humanPlayer.currentScore < self.computerPlayer.currentScore:
            print('Sorry, but you lost!')
        else:
            print('It is a draw...')