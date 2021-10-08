class BinaryCounter:

    def __init__(self, led4, led3, led2, led1):
        self.__led1 = led1
        self.__led2 = led2
        self.__led3 = led3
        self.__led4 = led4

    def asBinary(self):
        return str(self.__led4) + " " + str(self.__led3) + " " + str(self.__led2) + " " + str(self.__led1)
    
    def asHex(self):
        result = ""
        decimal = self.asDecimal()
        if decimal < 10:
            result = str(self.asDecimal())
        elif decimal == 10:
            result = 'A'
        elif decimal == 11:
            result = 'B'
        elif decimal == 12:
            result = 'C'
        elif decimal == 13:
            result = 'D'
        elif decimal == 14:
            result = 'E'
        elif decimal == 15:
            result = 'F'
        return result

    def asDecimal(self):
        decimal = 0
        if self.__led4 == 1:
            decimal += 8
        if self.__led3 == 1:
            decimal += 4
        if self.__led2 == 1:
            decimal += 2
        if self.__led1 == 1:
            decimal += 1

        return decimal



        

        

