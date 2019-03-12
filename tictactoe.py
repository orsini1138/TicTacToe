# tictactoe.py - a test to see if I can even make this fucking game lol
import numpy as np
import sys, sets


####################
#### DATA STUFF ####
####################

# PLAYER CHAR- SET LATER IN GAME LOOP WITH COUNT VAR
player = ''

# COUNT VAR INCRESES ++ EACH LOOP, PLAYER IS CHOSEN BY EVEN/ODD
count = 1

# VALID MAP CHOICES FOR PLAYER SELECTION
validChoices = ['1','2','3','4','5','6','7','8','9']

# MAP GRID AT GAME START
grid = np.array([['1',' | ','2',' | ','3'],
        ['-','-+-','-','-+-','-'],
        ['4',' | ','5',' | ','6'],
        ['-','-+-','-','-+-','-'],
        ['7',' | ','8',' | ','9']])



###################
#### GAME LOOP ####
###################

while True:
    
    # PRINT GAME MAP
    print('\n')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end='')
        print()

    # WINNING COMBINATIONS
    winners = [[grid[0][0], grid[0][2], grid[0][4]], #horizontal from l
           [grid[2][0], grid[2][2], grid[2][4]],
           [grid[4][0], grid[4][2], grid[4][4]],

           [grid[0][0], grid[2][0], grid[4][0]],     #vertical from top l
           [grid[0][2], grid[2][2], grid[4][2]],
           [grid[0][4], grid[2][4], grid[4][4]],

           [grid[0][0], grid[2][2], grid[4][4]],     #diagonals
           [grid[0][4], grid[2][2], grid[4][0]] 
            ]

    # WIN CONDITION
    for i in range(len(winners)):
        if len(set(winners[i])) == 1:
            print(f'\n--PLAYER {player} WINS--')
            input()
            sys.exit(0)

    # CATS GAME
    if count == 10:
        print('\n--CATS GAME--')
        input()
        sys.exit(0)

    # PLAYER ALTERNATION
    if count % 2 == 0:
        player = 'X'
    else:
        player = 'O'
  
    # PLAYER MOVE INPUT
    plInput = input(f'\nPLAYER {player}: ')
    
    # VALIDATE MOVE IS ON MAP
    if plInput not in validChoices:
        print('\nInvalid Option')
        input()
        continue
    # VALIDATE MAP POS IS NOT OCCUPIED
    elif plInput not in grid[0] and plInput not in grid[1] and plInput not in grid[2] and plInput not in grid[3] and plInput not in grid[4]:
        print('\nINVALID MOVE')
        input()
        continue
    else:
        # GET MAP POS COORDINATES W/ NUMPY
        movePos = np.where(grid == plInput)
        # CHANGE COORDINATES TO PLAYER CHAR
        grid[movePos[0][0]][movePos[1][0]] = player
    
    count += 1

