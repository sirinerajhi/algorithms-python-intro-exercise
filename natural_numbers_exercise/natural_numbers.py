class NaturalNumbers:

    def divideSevenAndNine(self):
        if (self % 7 == 0) and (self % 9 == 0):
            return True

    def sum(self):
        sum = 0
        for number in (0, 10000, 1):
            if number.divideSevenAndNine():
                sum += number
        return sum
