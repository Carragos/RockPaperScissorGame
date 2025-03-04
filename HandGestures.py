import sys
class HandGestures:
    def __init__(self):
        self.gestureNumber = 0

    def returnCheckBeat(self, handGesture):
        match self.gestureNumber:
            case 1:
                if (handGesture.gestureNumber == 3):
                    return 1
                elif (handGesture.gestureNumber == self.gestureNumber):
                    return 0
                else:
                    return -1
            case 2:
                if (handGesture.gestureNumber == 1):
                    return 1
                elif (handGesture.gestureNumber == self.gestureNumber):
                    return 0
                else:
                    return -1
            case 3:
                if (handGesture.gestureNumber == 2):
                    return 1
                elif (handGesture.gestureNumber == self.gestureNumber):
                    return 0
                else:
                    return -1 
            case _:
                print("Something went wrong...")
                print('Case was not successfully matched')
                sys.exit()


class Rock(HandGestures):
    def __init__(self):
        self.gestureNumber = 1

    def __str__(self):
        return "Rock 🪨"

class Paper(HandGestures):
    def __init__(self):
        self.gestureNumber = 2

    def __str__(self):
        return "Paper 📄"

class Scissors(HandGestures):
    def __init__(self):
        self.gestureNumber = 3

    def __str__(self):
        return "Scissors ✂️"