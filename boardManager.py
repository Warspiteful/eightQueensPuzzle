class boardManager:
    activeList = []
    solutions = []
    tween = []
    queenList = []
    
    def appendActive(self, queen):
           self.activeList.append([queen.x, queen.y]) 

    def getActive(self):
        return self.activeList

    def removeActive(self):
        self.activeList.pop()

    def saveSolution(self):
        tmp = self.activeList.copy()
        self.solutions.append(tmp)

    def getSolutions(self):
        return self.solutions

    


