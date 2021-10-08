class Point:
    #Constructor for Point
    def __init__(self, x, y):
        self.__xCoordinate = x
        self.__yCoordinate = y

    # Getters for X and Y coordinates
    def getX(self):
        return self.__xCoordinate
    
    def getY(self):
        return self.__yCoordinate
