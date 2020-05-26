class boardManager:
    #Class that handles tracking of positions for all queens

    #Holds list of current positions
    activeList = []
    
    #Holds all unique solutions in the form of tuples
    solutions = set([])
    
    #Create link to text file
    text_file = open("Output.txt", "w")

    #Method to add coordinates of a queen to list of current positions
    def appendActive(self, queen):
           self.activeList.append([queen.x, queen.y]) 

    #Returns list of coordinates of all appended queens
    def getActive(self):
        return self.activeList

    #Removes the last coordinates from the list of current positions
    def removeActive(self):
        self.activeList.pop()

    #Saves the current active list as a tuple to solutions
    def saveSolution(self):
        #Creates a copy of the list of current positions
        tmp = self.activeList.copy()
        
        #Converts list of coordinates into tuple and adds to solution set
        self.solutions.add(tuple(sorted(tuple(x) for x in tmp)))

        #Writes solution to text file
        self.text_file.write(str(tuple(sorted(tuple(x) for x in tmp))))
        self.text_file.write("\n")

    #Returns set of all solutions
    def getSolutions(self):
        return self.solutions

    


