"""
Simple TicTacToe v1.1
"""

#Defining the board. 3 rows with 3 cells
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#Player icons
p1_icon = "X"
p2_icon = "O"
#Player input
p_input_row = 0
p_input_cell = 0
#Player text
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
    """
    A function that checks the board. If no player won, the function will return false, meaning game isn't over.
    If player won, the function will return true, meaning game is over.
    """
    
    #Check vertical rows
    #First vertical row
    if board[0][0] == p1_icon and board[0][1] == p1_icon and board[0][2] == p1_icon:
        print(p1_won)
        return True
    elif board[0][0] == p2_icon and board[0][1] == p2_icon and board[0][2] == p2_icon:
        print(p2_won)
        return True
    #Second vertical row
    elif board[1][0] == p1_icon and board[1][1] == p1_icon and board[1][2] == p1_icon:
        print(p1_won)
        return True
    elif board[1][0] == p2_icon and board[1][1] == p2_icon and board[1][2] == p2_icon:
        print(p2_won)
        return True
    #Third vertical row
    elif board[2][0] == p1_icon and board[2][1] == p1_icon and board[2][2] == p1_icon:
        print(p1_won)
        return True
    elif board[2][0] == p2_icon and board[2][1] == p2_icon and board[2][2] == p2_icon:
        print(p2_won)
        return True
 
    #Check horizontal rows
    #First horizontal row
    if board[0][0] == p1_icon and board[1][0] == p1_icon and board[2][0] == p1_icon:
        print(p1_won)
        return True
    elif board[0][0] == p2_icon and board[1][0] == p2_icon and board[2][0] == p2_icon:
        print(p2_won)
        return True
    #Second horizontal row
    elif board[0][1] == p1_icon and board[1][1] == p1_icon and board[2][1] == p1_icon:
        print(p1_won)
        return True
    elif board[0][1] == p2_icon and board[1][1] == p2_icon and board[2][1] == p2_icon:
        print(p2_won)
        return True
    #Third horizontal row
    elif board[0][2] == p1_icon and board[1][2] == p1_icon and board[2][2] == p1_icon:
        print(p1_won)
        return True
    elif board[0][2] == p2_icon and board[1][2] == p2_icon and board[2][2] == p2_icon:
        print(p2_won)
        return True
    
    #Check diagonal rows:
    #Upper left to down right
    if board[0][0] == p1_icon and board[1][1] == p1_icon and board[2][2] == p1_icon:
        print(p1_won)
        return True
    elif board[0][0] == p2_icon and board[1][1] == p2_icon and board[2][2] == p2_icon:
        print(p2_won)
        return True
    #Down left to upper left
    elif board[2][0] == p1_icon and board[1][1] == p1_icon and board[0][2] == p1_icon:
        print(p1_won)
        return True
    elif board[2][0] == p2_icon and board[1][1] == p2_icon and board[0][2] == p2_icon:
        print(p2_won)
        return True
    
    #Check if board is full:
    if board[0][0] != 0 and board[0][1] != 0 and board[0][2] != 0 and board[1][0] != 0 and board[1][1] != 0 and board[1][2] != 0 and  board[2][0] != 0 and board[2][1] != 0 and board[2][2] != 0:
        print("Board is full!")
        return True 
    
    return False

#Function for player input
def player_turn(player):
    
    while True: #Loop for player turn
        if player == "p1" or player == "p2": #A player is chosen | p1 = Player 1 & p2 = Player 2
            if player == "p1":
                print("Player 1's turn")
            elif player == "p2":
                print("Player 2's turn")
            try: #Ask for player input
                p_input_row = int(input("Row: "))
                if p_input_row in [1, 2, 3]: #Correct row-input
                    p_input_cell = int(input("Cell: "))
                    if p_input_cell in [1, 2, 3]: #Correct cell-input
                        if board[(p_input_row - 1)][(p_input_cell - 1)] != p1_icon and board[(p_input_row - 1)][(p_input_cell - 1)] != p2_icon: #Check if cell is empty
                            if player == "p1": #Player 1 is chosen
                                board[(p_input_row - 1)][(p_input_cell - 1)] = p1_icon #Assign player icon to cell
                                print_board() #Print board
                                break #Break loop
                            elif player == "p2": #Player 2 is chosen
                                board[(p_input_row - 1)][(p_input_cell - 1)] = p2_icon
                                print_board()
                                break
                        else: #Cell is not empty
                            print(invalid)
                    else: #Invalid cell-input
                        print(invalid)
                else: #Invalid row-input
                    print(invalid)
            except ValueError: #Invalid player input 
                print(invalid)
        else: #Invalid player chosen
            print("[" + str(player) + "] is not a valid player!")
            break

#Display introduction message
print("Simple TicTacToe Project v1.1\n")
print("The board is created by 3 rows which includes 3 cells each.")
print("You have to choose a row and a cell to insert icon to board.\n")
print("Board:")
print("      ----------------------------")
print("Row 1 | Cell 1 | Cell 2 | Cell 3 |")
print("      ----------------------------")
print("Row 2 | Cell 1 | Cell 2 | Cell 3 |")
print("      ----------------------------")
print("Row 3 | Cell 1 | Cell 2 | Cell 3 |")
print("      ----------------------------")
print("Example: Left upper corner = Row: 1, Cell: 1\t\tCenter = Row: 2, Cell: 2\t Middle third row = Row: 3, Cell: 2\n")

#Main game-loop
while True:
    
    #Player 1's turn
    player_turn(player = "p1")
    game_over = check_board() #Check board
    
    if game_over == True: #Check game-state. Is game over?
        break #Exit main game-loop
    
    #Player 2's turn
    player_turn(player = "p2")
    game_over = check_board() #Check board
    
    if game_over == True:
        break
    
print("Game over!")


