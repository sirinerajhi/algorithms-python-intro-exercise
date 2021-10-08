from point import Point
import math

class Line:
    # Constructor of Line
    def __init__(self, pointA, pointB):
        self.__pointA = pointA
        self.__pointB = pointB

    # Method to calculate the length of the line with the Pythagoras formula

    def length(self):
        if self.__pointA.getY() > self.__pointB.getY():          
            aSide = self.__pointA.getY() - self.__pointB.getY()
        else:
            aSide = self.__pointB.getY() - self.__pointA.getY()
        
        if self.__pointA.getX() > self.__pointB.getX():
            bSide = self.__pointA.getX() - self.__pointB.getX()
        else:
            bSide = self.__pointB.getX() - self.__pointA.getX()
        
        cSide = math.sqrt((bSide**2) + (aSide**2))
        return cSide

    