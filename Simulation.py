from Person import Person

maxMoves = 2
dotsStock = 9

# Person(name of player, type of player "smart" or "random")
player1 = Person("player1S", "smart")
player2 = Person("player2S", "smart")

# Array of turns
order = [player1, player2]

# Simulation
while (dotsStock > 0):
    for player in order:
        if(dotsStock > 0):
            print(dotsStock)
            dotsStock = dotsStock - player.play(dotsStock, maxMoves)
            print("play: " + player.name)
        if(dotsStock <= 0):
            print("won: " + player.name)
            break
