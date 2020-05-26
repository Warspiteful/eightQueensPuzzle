from queens import *
from boardManager import *

board = [(i, j) for j in range(1,9) for i in range(1,9)]  

try:
    bm = boardManager()
    for x, y in board:
        if(queens([x,y]).canPlace(bm.getActive())):
            bm.appendActive(queens([x,y]))
            for x, y in board:
                if(queens([x,y]).canPlace(bm.getActive())):
                    bm.appendActive(queens([x,y]))
                    for x, y in board:
                        if(queens([x,y]).canPlace(bm.getActive())):
                            bm.appendActive(queens([x,y]))
                            for x, y in board:
                                if(queens([x,y]).canPlace(bm.getActive())):
                                    bm.appendActive(queens([x,y]))
                                    for x, y in board:
                                        if(queens([x,y]).canPlace(bm.getActive())):
                                            bm.appendActive(queens([x,y]))
                                            for x, y in board:
                                                if(queens([x,y]).canPlace(bm.getActive())):
                                                    bm.appendActive(queens([x,y]))
                                                    for x, y in board:
                                                        if(queens([x,y]).canPlace(bm.getActive())):
                                                            bm.appendActive(queens([x,y]))
                                                            for x, y in board:
                                                                if(queens([x,y]).canPlace(bm.getActive())):
                                                                    bm.appendActive(queens([x,y]))
                                                                    solCheck = tuple(sorted(tuple(x) for x in bm.getActive()))
                                                                    if(solCheck not in bm.getSolutions()):
                                                                        bm.saveSolution()
                                                                    bm.removeActive()
                                                            bm.removeActive()
                                                    bm.removeActive()
                                            bm.removeActive()
                                    bm.removeActive()
                            bm.removeActive()
                    bm.removeActive()
            bm.removeActive()
    print(len(set(bm.getSolutions())))
except IndexError:
    print(len(set(bm.getSolutions())))
    

