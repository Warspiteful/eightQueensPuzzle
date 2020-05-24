class queens:

    def __init__(self, coords):
        self.x, self.y = coords

    

    def canPlace(self,QueensList):
        for coords in QueensList:
            
            if (self.x == coords[0] or self.y == coords[1] or abs( coords[0]- self.x) == abs( coords[1]- self.y)):
                return False
        return True
            
              