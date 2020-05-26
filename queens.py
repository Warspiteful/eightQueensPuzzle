class queens:
    #Class that represents a queen on a chess board

    #Initialize with position coordinates
    def __init__(self, coords):
        self.x, self.y = coords

    #Checks if position of queen is valid given all other placed queens
    def canPlace(self,QueensList):
        #Iterates through the coordinates of all currently placed queens
        for coords in QueensList:
            #Checks horizontal, vertical, or diagonal are shared
            if (self.x == coords[0] or self.y == coords[1] or abs(coords[0] - self.x) == abs(coords[1] - self.y)):
                #If threatened, can not be placed
                return False
        #If not threatened by any currently placed queens, can be placed
        return True
            
              