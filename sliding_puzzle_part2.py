# Mattieux Fournier 2445249
import random
import sys
# dictionary for user if inputs are yes or no
dict = {'YES': 'Y', 'NO': 'N'}
def tileLabels(n):
    lst = [f'{i:2}' for i in range(1, (n**2))]
    lst.append('  ')
    return lst

def getNewPuzzle(n):
    tiles = tileLabels(n)
    random.shuffle(tiles)
    board = [tiles[i:i+n] for i in range(0,len(tiles),n)]
    return board

def findEmptyTile(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '  ':
                return (row,col)
# checks for puzzle completement
def isWon(board):
    win = [f'{i:2}' for i in range(1, len(board)**2)]
    win.append('  ')
    fullBoard = [tile for row in board for tile in row]
    if win == fullBoard:
        displayBoard(board)
        print("Congratulations! You won!")
        return True
    return False

def nextMove(n):
    board = getNewPuzzle(n)
    while not isWon(board):
        row, col = findEmptyTile(board)
        displayBoard(board)
        moves = f"   (W)\n(A)(S)(D) or (Quit)"
        if col == n-1:
            moves = moves.replace("(A)","( )")
        if col == 0:
            moves = moves.replace("(D)","( )")
        if row == n-1:
            moves = moves.replace("(W)","( )")
        if row == 0:
            moves = moves.replace("(S)", "( )")
        print(f'valid moves: \n{moves}')
        move = input("Enter valid move: ").strip().upper()
        print(f'You chose: {move}')
        new_row, new_col = row, col
        if move == "A" and col < n-1:
            new_col += 1
        elif move == "D" and col > 0:
            new_col -= 1
        elif move == "W" and row < n-1:
            new_row += 1
        elif move == "S" and row > 0:
            new_row -= 1
        elif move == "QUIT":
            sys.exit()
        else:
            print("That move is not valid!")
       
        board[row][col], board[new_row][new_col] = board[new_row][new_col], board[row][col]
    else:
        #if user wants to re-run the game without restarting the program
        replay()

def displayBoard(board):
    n = len(board)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

def welcomeMessage():
    print("Welcome to Tile Slide!\nThe goal is to rearrange the tiles in increasing order from left to right.")
    while True:
        user = input("Would you like to play?(Y/N): ").strip().upper()
        # in case user tries yes or no it recognizes it as valid
        if user in dict:
            user = dict[user]
        if user == "Y":
            startGame()
        elif user == "N":
            print("See you next time!")
            sys.exit()
        else:
            print("Sorry that's not a valid option!")
#starts game based on user input for welcome message
def startGame():
    while True:
        n = input("What dimensions would you like for your grid (nxn) or quit? n = ").strip()
        # in case user does not input an integer so it does not return a type error
        try:
            n = int(n)
            if n <= 2:
                print("Grid is too small!")
            else:
                return nextMove(n)
        except ValueError:
            print("Sorry that's not a number!")
#function that initiates a replay prompt
def replay():
    while True:
        restart = input("Would you like to play again? (Y/N): ").strip().upper()
        # in case user inputs yes or no instead it recognizes it as valid
        if restart in dict:
            restart = dict[restart]
        if restart == "Y":
            startGame()
        elif restart == "N":
            print("See you next time!")
            sys.exit()
        else:
            print("Sorry that's not a valid option!")
welcomeMessage()