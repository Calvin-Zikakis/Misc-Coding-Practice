#!/usr/bin/env python
# coding: utf-8

# In[111]:


#imports
import numpy as np


# In[112]:


#need a 3x3 board for tik tac toe
#this resets the board
def reset():
    board = np.array([".",".",".",".",".",".",".",".",".",]).reshape(3,3)
    return board


# In[113]:


#need the function to add a move
#inputs - player (x or o), board, row for move, column for move
#outputs - if move was success or not and the board

def play(player, board):
    row, column = input("Enter a row and column seperated by a space: ").split()
    print("row: ", int(row))
    print("column: ", int(column))
    print()
    row = int(row) - 1
    column = int(column) - 1
    
    if row > 3 or row < 0 or column > 3 or column < 0:
        print("Not a valid location")
        return False, board
    
    if board[row, column] == ".":
        board[row, column] = player
        print("Move was successful")
        return True, board
    
    elif board[row, column] == "X" or board[row, column] == "O":
        print("Player already at that location")
        return False, board
        



# In[114]:


#need a function to check for a win
#takes an input of the board
#outputs true or false
def win(board):
    
    if board [0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ".":
    #checks if there is a winner on the first diag
        return True
    
    elif board [0][2] == board[1][1] and board[1][1] == board[2][1] and board[1][1] != ".":
    #checks if there is a winner on the sec diag
        return True
    
    
    for i in range(3):
        
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != ".":
        #checks if there is a winner on the rows
            return True
        
        elif board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != ".":
        #checks if there is a winner on the columns
            return True

    return False


# In[ ]:


#need a function to drive the game
turn = 0
moves = 0

player_1 = "X"
player_2 = "O"

board = reset()
winner = False

while not winner:
    print(board)
    valid = False
    
    if turn == 0:
        player = player_1
        print(player_1, "'s turn.")
        turn = 1
    else:
        player = player_2
        print(player_2, "'s turn.")
        turn = 0
    

    
    while not valid:
        valid, board = play(player, board)
    winner = win(board)
    if winner:
        print(player, "'s Win!'")
        print(board)
        
    if turn == 9:
        print("Cat's Game")
        break


    turn += 1
    
    


# In[ ]:




