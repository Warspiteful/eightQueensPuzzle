from queens import *
from boardManager import *

board = [(i, j) for j in range(1,9) for i in range(1,9)]  

bm = boardManager()



for x, y in board:
    if(queens([x,y]).canPlace(bm.getActive())):
        bm.appendActive(queens([x,y]))
        bm.saveSolution(bm.getActive())
        print(bm.getSolutions())
        bm.removeActive()
        print(bm.getSolutions())

