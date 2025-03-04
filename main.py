from Game import Game
def main():
    # gui = MyGUI()       
    # # This call blocks and runs the GUI event loop
    # gui.run_ui(dark=True, native=True)

    myGame = Game()
    myGame.startGame()

    for i in range (myGame.gameRounds):
        myGame.playRound()
    
    myGame.finalScoreAnalysis()

if __name__ in {"__main__", "__mp_main__"}:
    main()