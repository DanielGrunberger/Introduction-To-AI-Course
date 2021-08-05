import copy
import alphaBetaPruning
import random

VICTORY=10**20 #The value of a winning board (for max) 
LOSS = -VICTORY #The value of a losing board (for max)
TIE=0 #The value of a tie
SIZE=4 #the length of winning seq.
COMPUTER=SIZE+1 #Marks the computer's cells on the board
HUMAN=1 #Marks the human's cells on the board

rows=6
columns=7

class game:
    board=[]
    size=rows*columns
    playTurn = HUMAN
    
     #Used by alpha-beta pruning to allow pruning

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''

def create(s):
        #Returns an empty board. The human plays first.
        #create the board
        s.board=[]
        for i in range(rows):
            s.board = s.board+[columns*[0]]
        
        s.playTurn = HUMAN
        s.size=rows*columns
        s.val=0.00001
    
        #return [board, 0.00001, playTurn, r*c]     # 0 is TIE

def cpy(s1): # Create a copy of s1 board and returns it
        # construct a parent DataFrame instance
        s2=game()
        s2.playTurn = s1.playTurn
        s2.size=s1.size
        s2.board=copy.deepcopy(s1.board)
        #print("board ", s2.board)
        return s2
       
def value(s):
#Returns the heuristic value of s
    dr=[-SIZE+1, -SIZE+1, 0, SIZE-1] #the next lines compute the heuristic val.
    dc=[0, SIZE-1, SIZE-1, SIZE-1]
    val=0.00001
    for row in range(rows):
        for col in range(columns):
            for i in range(len(dr)):
                t=checkSeq(s, row, col, row+dr[i], col+dc[i])
                if t in [LOSS,VICTORY]:
                   val=t
                   break
                else:
                   val+=t
    if s.size==0 and val not in [LOSS, VICTORY]:
       val=TIE
    return val
        
        
"""
We added a verification like that: If we have only human on the sequence, we give a small negative value for 2 pieces in sequence,
because it is a good thing for human but not so good since it is only two. If we have 3, we give a much smaller negative value, since
3 in  a row is very good (almost victory)
The same thing for the computer, but giving high positive values. If the computer has 2 or 3 pieces in a row, it is bad for human, so
we give a high positive value.
"""
def checkSeq(s, r1, c1, r2, c2):
#r1, c1 are in the board. if r2,c2 not on board returns 0.
#Checks the seq. from r1,c1 to r2,c2. If all X returns VICTORY. If all O returns LOSS.
#If empty returns 0.00001. If no Os returns 1. If no Xs returns -1.
    if r2<0 or c2<0 or r2>=rows or c2>=columns:
        return 0 #r2, c2 are illegal

    dr=(r2-r1)//(SIZE-1) #the horizontal step from cell to cell
    dc=(c2-c1)//(SIZE-1) #the vertical step from cell to cell

    sum=0

    for i in range(SIZE):#summing the values in the seq.
        sum += s.board[r1+i*dr][c1+i*dc]

    if sum == COMPUTER*SIZE:
        return VICTORY

    elif sum == HUMAN*SIZE:
        return LOSS

    if sum > 0:
        if COMPUTER > sum: # there is only human pieces
            if sum == HUMAN * 2: # Two human pieces
                return  sum*-20
            elif sum == HUMAN * 3: # 3 human pieces
                return sum*-200
            return -1

        elif sum % COMPUTER == 0: # Only computer pieces
            if sum == COMPUTER * 2: # Two computer pieces
                return sum*20
            elif sum == COMPUTER * 3: # 3 computer pieces
                return sum*200
            return 1
    return 0.00001  # not 0 because TIE is 0


"""


"""


def printState(s):
#Prints the board. The empty cells are printed as numbers = the cells name(for input)
#If the game ended prints who won.
        for r in range(rows):
            print("\n|",end="")
            for c in range(columns):
                if s.board[r][c]==COMPUTER:
                    print("X|", end="")
                elif s.board[r][c]==HUMAN:
                    print("O|", end="")
                else:
                    print(" |", end="")
        print()

        for i in range(columns): #For numbers on the bottom
            print(" ",i,sep="",end="")

        print()
        
        val=value(s)

        if val==VICTORY:
            print("I won!")
        elif val==LOSS:
            print("You beat me!")
        elif val==TIE:
            print("It's a TIE")

def isFinished(s):
#Seturns True iff the game ended
        return value(s) in [LOSS, VICTORY, TIE] or s.size==0


def isHumTurn(s):
#Returns True iff it is the human's turn to play
        return s.playTurn==HUMAN
    

def decideWhoIsFirst(s):
#The user decides who plays first
        if int(input("Who plays first? 1-me / anything else-you : "))==1:
            s.playTurn=COMPUTER
        else:
            s.playTurn=HUMAN          
        return s.playTurn
        

def makeMove(s, c):
#Puts mark (for humaמ or computer) in col. c
#and switches turns.
#Assumes the move is legal.
        r=0
        while r<rows and s.board[r][c]==0:
            r+=1

        s.board[r-1][c]=s.playTurn # marks the board
        s.size -= 1 #one less empty cell
        if (s.playTurn == COMPUTER ):
            s.playTurn = HUMAN
        else:
            s.playTurn = COMPUTER
  
def inputMove(s):
#Reads, enforces legality and executes the user's move.
        flag=True
        while flag:
            c=int(input("Enter your next move: "))
            if c<0 or c>=columns or s.board[0][c]!=0:
                print("Illegal move.")
            else:
                flag=False
                makeMove(s,c)

def inputRandom(s):
    for i in range(0, columns):  # this simple agent always plays min
        tmp = cpy(s)
        makeMove(tmp, i)
        if (value(tmp) == LOSS and s.board[0][i] == 0):  # so a "loss" is a win for this side
            makeMove(s, i)
            return
    # If no obvious move, than move random
    flag = True
    while flag:
        c = random.randrange(0, columns)
        if c < 0 or c >= columns or s.board[0][c] != 0: # Checks if it is a legal move
            print("Illegal move.")
            printState(s)
        else: # If it is legal, make the move
            flag = False
            makeMove(s, c)
        
def getNext(s):
#returns a list of the next states of s
        ns=[]
        for c in list(range(columns)):
            # print("c=",c) # Prints the current move number
            if s.board[0][c]==0:
                # print("possible move ", c)
                tmp=cpy(s)
                makeMove(tmp, c)
                # print("tmp board=",tmp.board) # Prints the board after making this move
                ns+=[tmp]
                # print("ns=",ns) # Prints hte list with all the moves
        return ns

def inputComputer(s):    
        return alphaBetaPruning.go(s)
