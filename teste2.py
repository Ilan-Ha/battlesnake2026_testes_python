import board as BModule
import snake as SModule
from player import Player as PM
import time
def separation():
    print('--'*size)

size = 11
b = BModule.Board(size)
s1 = SModule.Snake()
p1 = PM(s1)
s2 = SModule.Snake()
p2 = PM(s2)
s3 = SModule.Snake()
p3 = PM(s3)
s4 = SModule.Snake()
p4 = PM(s4)
players = b.players
s1.start([[0,0],[0,1],[0,2],[1,2]])
s2.start([[4,4],[4,3],[4,2],[3,2]])
s3.start([[10,10],[10,9],[10,8],[9,8],[8,8]])
s4.start([[6,6],[6,5]])

# b.printBoard()
# separation()
b.addPlayers([p1,p2,p3,p4])
b.mapIndex()
b.updateBoard()
# print(b.index)
while(players.__len__()>0):
    b.printBoard()
    b.move()
    separation()
    # time.sleep(1/120)

b.printBoard()

#print(dir(s))
#print(s.__dict__)

# b.mapIndex()
# b.printBoard()

# key = '(1,2)'
# x,y = key.strip("()").split(',')
# print(x)
# print(y)

