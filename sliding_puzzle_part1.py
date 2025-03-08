import random
import sys

def tileLabels(n):
    lst = [str(i) for i in range(1, (n**2))]
    lst.append("  ")
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
            
def nextMove(n):
    board = getNewPuzzle(n)
    while True:
        move = ''
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
        print(f'Your last move was: {move}')
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
            print("Invalid move")
       
        board[row][col], board[new_row][new_col] = board[new_row][new_col], board[row][col]
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
nextMove(int(input("n: ")))



