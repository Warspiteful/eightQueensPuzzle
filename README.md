# Eight Queens Puzzle
Personal Project suggested as a programming exercise to build familiarity with algorithims and data structures. Made blind without any prior research on existing solutions.

## Prompt 
The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal.

## About My Code
The problem was tackled in Python, my most comfortable language. I approached this problem with the idea of sets and loops with Depth-First Search process, exhausting all possible solutions for the last piece before moving the second-to-last piece and so-on-and-so-forth. This resulted in a lot of loops in my main file, which I have not been able to streamline successfully. 

## Classes
### Class: 
`Queens` - Represents Queen Piece
* canPlace(self,QueensList)

`boardManager` - Handles all tracking, builds solution sets and writes them to text file
* AppendActive(self)
* getActive(self)
* removeActive(self)
* saveSolution(self)
* getSolutions(self)

`Puzzle` - Contains Solving Loop, File to Run

## Results
Takes around 2 hours to finish processing all 92 solutions
Upon reflection, this problem taught me a lot about object-oriented programming and the reason why it has become so important
