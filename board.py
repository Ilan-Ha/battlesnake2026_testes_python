from player import Player as PModule
from choices import Choices as CE

class Board:
    size: int
    board: list[list[int]]
    players: list[PModule]
    index: dict[str:str]
    keys: set[str]
    gamestate: dict
    def __init__(self,size:int):
        self.size = size
        self.board = list()
        self.players = list()
        self.index = dict()
        self.keys = set()
        self.gamestate = {'size': self.size,'players':self.players}
        self.createIndex()
        self.createBoard()


    def createIndex(self):
        for x in range(self.size):
            for y in range(self.size):
                self.index.update({f'({x},{y})':'◌'})

    def createBoard(self):
        #print(self.index)
        for x in range(self.size):
            self.board.append([])
            for y in range(self.size):
                self.board[x].append(self.index.get(f'({x},{y})','◌'))

    def updateBoard(self):
        for key in self.keys:
            x,y = key.strip("()").split(',')
            cat = self.index.get(key,'◌')
            self.board[int(x)][int(y)] = cat
            if cat == '◌':
                self.keys.remove(key)

    def move(self):
        to_delete: list[PModule] = list()
        for player in self.players:
            #print(snake.__dict__)
            snake = player.snake
            tail:list[int] = snake.tail.copy()
            head:list[int] = snake.head.copy()
            coor = f'({tail[0]},{tail[1]})'
            self.index[coor] = '◌'
            self.keys.remove(coor)
            self.board[tail[0]][tail[1]] = '◌'
            choice: str = player.choice(self.gamestate)
            #print(choice)
            self.playerChoice(head,choice)
            if(not self.check(head)):
                to_delete.append(player)
            else:
                player.move(head)
        for player in to_delete:
            self.removePLayer(player)
        self.mapIndex()
        self.updateBoard()

    def check(self,head: list[int]):
        return(head[0] in range(self.size) and head[1] in range(self.size))

    def removePLayer(self,pl: PModule):
        #print(self.keys)
        snk = pl.snake
        coordinates = snk.coordinates
        for n in range(snk.size):
            row = coordinates[n]
            coor = f'({row[0]},{row[1]})'
            cat = self.index.get(coor,'◌')
            if(cat != '◌'):    
                self.index[coor] = '◌'
                self.keys.remove(coor)
                self.board[row[0]][row[1]] = '◌'
        self.players.remove(pl)
    
    def mapIndex(self):
        i: int = 0
        for player in self.players:
            i += 1
            snake = player.snake
            #print(snake)
            size = snake.size
            #print(size)
            coordinates = snake.coordinates
            #print(coordinates)
            for n in range(size):
                row = coordinates[n]
                #print(row)
                cat = u'\u001b[38;5;'
                if n == 0:
                    cat += str(i) + u'm▣\u001b[0m'
                else:
                    cat += str(i) + u'm▦\u001b[0m'
                coo = f'({row[0]},{row[1]})'
                #print(coo)
                self.index.update({coo:cat})
                self.keys.add(coo)

    def addPlayers(self,players:list[PModule]):
        for pl in players:
            self.players.append(pl)
        
    def printBoard(self):
        for row in self.board:
            aux = ''
            for it in row:
                aux = f'{aux} {it}'
            print(aux)

    def playerChoice(self,head: list[int],choice: str):
        match choice:
            case CE.UP:
                head[0] -= 1
                return 
            case CE.DOWN:
                head[0] += 1
                return
            case CE.LEFT:
                head[1] -= 1
                return 
            case CE.RIGHT:
                head[1] += 1
                return