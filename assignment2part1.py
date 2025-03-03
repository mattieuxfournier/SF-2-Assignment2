import random
n = int(input("enter n: "))
def titleLabels(n):
    lst = [str(i) for i in range(1, (n**2))]
    lst.append("  ")
    return lst, n
def getNewPuzzle(lst, n):
    random.shuffle(titleLabels(n))
    board = []
    for a in range(n):
        line = []
        for i in range(n): 
            line.append(lst[i+a*n])
        board.append(line)
    return board
def findEmptyTile(n):
    board = getNewPuzzle(n)
    print(board)
    for j in range(len(board)):
        for i in range(n):
            if board[j][i] == '  ':
                position = (j+1,i+1)
                return position
    print(board)
    
def nextMove(n):
    position = findEmptyTile(n)
    for i in range(0,2):
        if position[i] == 1:
            input("W", "A", " ", "S")



