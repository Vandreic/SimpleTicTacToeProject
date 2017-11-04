"""
Simple TicTacToe v1.0
"""

#Defining the board. 3 rows with 3 cells
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#Game-state
game_over = False

#Player icons
p1_icon = "X"
p2_icon = "O"

#Player input
p1_input_row = 0
p1_input_cell = 0
p2_input_row = 0
p2_input_cell = 0
#Player text
p1_turn = "Player 1's turn: "
p2_turn = "Player 2's turn: "
p1_won = "Player 1 won!"
p2_won = "Player 2 won!"

#String for invalid answer
invalid = "Invalid answer! Try again.\n"

#Function for printing the board
def print_board():
    print("\n-------")
    print("|" + str(board[0][0]) + "|" + str(board[0][1]) + "|" + str(board[0][2]) + "|")
    print("-------")
    print("|" + str(board[1][0]) + "|" + str(board[1][1]) + "|" + str(board[1][2]) + "|")
    print("-------")
    print("|" + str(board[2][0]) + "|" + str(board[2][1]) + "|" + str(board[2][2]) + "|")
    print("-------\n")

#Function for checking the board
def check_board():
    
    #Check horizontal rows
    #First horizontal row
    if board[0][0] and board[1][0] and board[2][0] == p1_icon:
        print(p1_won)
    elif board[0][0] and board[1][0] and board[2][0] == p2_icon:
        print(p2_won)
    #Second horizontal row
    elif board[0][1] and board[1][1] and board[2][1] == p1_icon:
        print(p1_won)
    elif board[0][1] and board[1][1] and board[2][1] == p2_icon:
        print(p2_won)
    #Third horizontal row
    elif board[0][2] and board[1][2] and board[2][2] == p1_icon:
        print(p1_won)
    elif board[0][2] and board[1][2] and board[2][2] == p2_icon:
        print(p2_won)
    
    #Check diagonal rows:
    #Upper left to down right
    if board[0][0] and board[1][1] and board[2][2] == p1_icon:
        print(p1_won)
    elif board[0][0] and board[1][1] and board[2][2] == p2_icon:
        print(p2_won)
    #Down left to upper left
    elif board[2][0] and board[1][1] and board[0][2] == p1_icon:
        print(p1_won)
    elif board[2][0] and board[1][1] and board[0][2] == p2_icon:
        print(p2_won)

#Main game-loop
while True:
    #Loop for player 1's turn
    while True:
        #Player 1's turn
        print(p1_turn)
        p1_input_row = int(input("Row: "))
        #Check player 1's input
        if p1_input_row in [1, 2, 3]: #Correct row-input
            p1_input_cell = int(input("Cell: "))
            if p1_input_cell in [1, 2, 3]: #Correct cell-input
                if board[(p1_input_row - 1)][(p1_input_cell - 1)] != p1_icon and board[(p1_input_row - 1)][(p1_input_cell - 1)] != p2_icon: #Check if cell is empty
                    board[(p1_input_row - 1)][(p1_input_cell - 1)] = p1_icon
                    print_board()
                    
                    #Check vertical rows
                    #First vertical row
                    if board[0][0] and board[0][1] and board[0][2] == p1_icon:
                        print(p1_won)
                        game_over = True
                        break
                    #Second vertical row
                    elif board[1][0] and board[1][1] and board[1][2] == p1_icon:
                        print(p1_won)
                        game_over = True
                        break
                    #Third vertical row
                    elif board[2][0] and board[2][1] and board[2][2] == p1_icon:
                        print(p1_won)
                        game_over = True
                        break
                        
                    #Check horizontal rows
                    #First horizontal row
                    if board[0][0] and board[1][0] and board[2][0] == p1_icon:
                        print(p1_won)
                        game_over = True
                        break
                    #Second horizontal row
                    elif board[0][1] and board[1][1] and board[2][1] == p1_icon:
                        print(p1_won)
                        game_over = True
                        break
                    #Third horizontal row
                    elif board[0][2] and board[1][2] and board[2][2] == p1_icon:
                        print(p1_won)
                        game_over = True
                        break
                    
                    #Check diagonal rows:
                    #Upper left to down right
                    if board[0][0] and board[1][1] and board[2][2] == p1_icon:
                        print(p1_won)
                        game_over = True
                        break
                    #Down left to upper left
                    elif board[2][0] and board[1][1] and board[0][2] == p1_icon:
                        print(p1_won)
                        game_over = True
                        break
                    break
                    
                else: #Cell is not empty
                    print(invalid)
            else: #Invalid cell-input
                print(invalid)
        else: #Invalid row-input
            print(invalid)
    
    #If game is over, break loop
    if game_over == True:
        break
    
    #Loop for player 2's turn
    while True:
        #Player 2's turn
        print(p2_turn)
        p2_input_row = int(input("Row: "))
        #Check player 2's input
        if p2_input_row in [1, 2, 3]: #Correct row-input
            p2_input_cell = int(input("Cell: "))
            if p2_input_cell in [1, 2, 3]: #Correct cell-input
                if board[(p2_input_row - 1)][(p2_input_cell - 1)] != p1_icon and board[(p2_input_row - 1)][(p2_input_cell - 1)] != p2_icon: #Check if cell is empty
                    board[(p2_input_row - 1)][(p2_input_cell - 1)] = p2_icon
                    print_board()
                    
                    #Check vertical rows
                    #First vertical row
                    if board[0][0] and board[0][1] and board[0][2] == p2_icon:
                        print(p2_won)
                        game_over = True
                        break
                    #Second vertical row
                    elif board[1][0] and board[1][1] and board[1][2] == p2_icon:
                        print(p2_won)
                        game_over = True
                        break
                    #Third vertical row
                    elif board[2][0] and board[2][1] and board[2][2] == p2_icon:
                        print(p2_won)
                        game_over = True
                        break
                        
                    #Check horizontal rows
                    #First horizontal row
                    if board[0][0] and board[1][0] and board[2][0] == p2_icon:
                        print(p2_won)
                        game_over = True
                        break
                    #Second horizontal row
                    elif board[0][1] and board[1][1] and board[2][1] == p2_icon:
                        print(p2_won)
                        game_over = True
                        break
                    #Third horizontal row
                    elif board[0][2] and board[1][2] and board[2][2] == p2_icon:
                        print(p2_won)
                        game_over = True
                        break
                    
                    #Check diagonal rows:
                    #Upper left to down right
                    if board[0][0] and board[1][1] and board[2][2] == p2_icon:
                        print(p2_won)
                        game_over = True
                        break
                    #Down left to upper left
                    elif board[2][0] and board[1][1] and board[0][2] == p2_icon:
                        print(p2_won)
                        game_over = True
                        break
                    break
                    
                else: #Cell is not empty
                    print(invalid)
            else: #Invalid cell-input
                print(invalid)
        else: #Invalid row-input
            print(invalid)
        
    #If game is over, break loop
    if game_over == True:
        break

print("Game over!")


