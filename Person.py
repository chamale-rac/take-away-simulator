
import randomPlayer
import smartPlayer


class Person:
    def __init__(self, name, playerType):
        self.name = name
        self.playerType = playerType

    def play(self, dotsStock, maxMoves):
        if(self.playerType == "random"):
            return randomPlayer.play(dotsStock, maxMoves)
        elif(self.playerType == "smart"):
            return smartPlayer.play(dotsStock, maxMoves)
