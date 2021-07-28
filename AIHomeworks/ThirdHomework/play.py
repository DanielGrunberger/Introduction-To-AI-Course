# Royi Alishayev 211503701
# Daniel Grunberger 522883
import alphaBetaPruning
import game

board=game.game()
game.create(board)
print("Initial Game")
game.printState(board)
game.decideWhoIsFirst(board)
comp_count = 0
for i in range(0,100):
#for i in range(0,50): 
    while not game.isFinished(board):
        if game.isHumTurn(board):
            game.inputRandom(board)
            #game.inputMove(board)
        else:
            board=alphaBetaPruning.go(board)
        game.printState(board)
    if game.value(board)==10**20: #the computer (or smart agent) won
        comp_count+=1
    print("Start another game")
    game.create(board)
print("The agent beat you:", comp_count, " out of ", i+1)

