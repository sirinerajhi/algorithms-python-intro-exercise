from line import Line
from point import Point
import math

def test_length():

    pointA = Point(2,4)
    pointB = Point(1,2)
    line = Line(pointA, pointB)
    assert(line.length() == math.sqrt(5))