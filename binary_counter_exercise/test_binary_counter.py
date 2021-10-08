from binary_counter import BinaryCounter

def test_natural():
    number = BinaryCounter(1,1,1,0)
    decimal = number.asDecimal()
    hex = number.asHex()
    binary = number.asBinary()
    assert(decimal == 14)
    assert(hex == "E")
    assert(binary == "1 1 1 0")