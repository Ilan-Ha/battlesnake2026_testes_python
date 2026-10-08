import time

board = []
size = 11
for x in range(size):
    board.append([])
    for y in range(size):
        board[x].append('◌')

def separation():
    print('--'*size)

def printMap():
    global board
    for row in board:
        aux = ''
        for it in row:
            aux = f'{aux} {it}'
        print(aux)
    separation()

alive: bool = True
snk: list[list[int]] = [[1,2],[1,3],[0,3]]

alive2: bool = True
snk2: list[list[int]] = [[0,8],[0,7],[0,6],[0,5]]

def registerSnk(snk: list[list[int]]):
    global board
    for n in range(len(snk)):
        row = snk[n]
        if n == 0:
            cat = '▣'
        else:
            cat = '▦'
        board[size-row[0]-1][row[1]] = cat

def check(head: list[int]):
    return(head[0] in range(size) and head[1] in range(size))

def removeSnk(snk: list[list[int]]):
    global board
    for n in range(len(snk)):
        row = snk[n]
        board[size-row[0]-1][row[1]] = '◌'

def move(snk: list[list[int]], new: list[int]):
    if(not check(new)):
       return False
    siz = len(snk)
    removeSnk(snk)
    for n in range(siz-1):
        snk[siz-n-1] = snk[siz-n-2].copy()
    snk[0] = new.copy()
    return True


mov: list[int]
while(alive or alive2):
    if(alive):
        registerSnk(snk)

    if(alive2):
        registerSnk(snk2)
    printMap()
    time.sleep(0.5)
    if(alive):
        mov = snk[0].copy()
        mov[0] += 1
        alive = move(snk,mov)
        if(not alive):
            removeSnk(snk)
    if(alive2):
        mov = snk2[0].copy()
        mov[0] += 1
        alive2 = move(snk2,mov)
        if(not alive2):
            removeSnk(snk2)


time.sleep(0.5)
printMap()

