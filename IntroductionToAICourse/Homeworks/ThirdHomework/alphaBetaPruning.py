import game
DEPTH=2
def go(gm):
    #print("In go of game ", gm.board)
    if game.isHumTurn(gm): # if its the human's turn then we gonna activate the minimum alpha beta method.
        #print("Turn of human")
        obj= abmin(gm, DEPTH, game.LOSS-1, game.VICTORY+1)[1]
        #print("object board: ",obj.board)
        return obj
    else: # if its the computer's turn then we gonna activate the maximum alpha beta method.
        #print("Turn of agent")
        obj= abmax(gm, DEPTH, game.LOSS-1, game.VICTORY+1)[1]
        #print("object board: ",obj.board)
        return obj


def abmax(gm, d, a, b):
    #print("now calculate abmax")
    #print("d=",d) # The depth
    #print("alpha=",a)
    #print("beta=",b)
    if d==0 or game.isFinished(gm):
        return [game.value(gm),gm]
    v=float("-inf")
    ns=game.getNext(gm)
    #print("next moves:", len(ns), " possible moves ")
    bestMove=0
    for st in ns:
        tmp=abmin(st,d-1,a,b)
        if tmp[0]>v:
            v=tmp[0]
            bestMove=st
        if v>=b:
            return [v,st]
        if v>a:
            a=v
    return [v,bestMove]


def abmin(gm, d, a, b):
    #print("now calculate abmin")
    #print("d=",d)
    #print("a=",a)
    #print("b=",b)
    
    
    if d==0 or game.isFinished(gm):
        #print("returns ", [game.value(gm), gm])
        return [game.value(gm),0]
    v=float("inf")
    
    
    ns=game.getNext(gm)
    #print("next moves:", len(ns), " possible moves ")
    bestMove=0
    for st in ns:
        tmp = abmax(st, d - 1, a, b)
        if tmp[0]<v:
            v = tmp[0]
            bestMove = st
        if v <= a:
            return [v,st]
        if v < b:
            b = v
    return [v, bestMove]
