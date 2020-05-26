#Eight Queen Puzzle
#Created by Justin Almendral
#Date Started: May 22 2020

#Imports classes
from queens import *
from boardManager import *

#Creates an 8x8 board
board = [(i, j) for j in range(1,9) for i in range(1,9)]  

#Initialize Board Manager Class
bm = boardManager()

#Iterate through all (x,y) of the 8x8 board - Definitely some way to optimize it with a method and recursion, just haven't gotten around to it
for x, y in board: #Loops through all possible positions for 1st piece
    if(queens([x,y]).canPlace(bm.getActive())): #Checks if is valid placement
        bm.appendActive(queens([x,y])) #Appends position to active list

        for x, y in board: #Second Piece Loops
            if(queens([x,y]).canPlace(bm.getActive())):
                bm.appendActive(queens([x,y]))

                for x, y in board: #Third Piece Loops
                    if(queens([x,y]).canPlace(bm.getActive())):
                        bm.appendActive(queens([x,y]))

                        for x, y in board: #Fourth Piece Loop
                            if(queens([x,y]).canPlace(bm.getActive())):
                                bm.appendActive(queens([x,y]))

                                for x, y in board: #Fifth Piece Loop
                                    if(queens([x,y]).canPlace(bm.getActive())):
                                        bm.appendActive(queens([x,y]))

                                        for x, y in board: #Sixth Piece Loop
                                            if(queens([x,y]).canPlace(bm.getActive())):
                                                bm.appendActive(queens([x,y]))
                                                
                                                for x, y in board: #Seventh Piece Loop
                                                    if(queens([x,y]).canPlace(bm.getActive())):
                                                        bm.appendActive(queens([x,y]))

                                                        for x, y in board: #Eighth Piece Loop
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

    

