from random import randint, choice


# Generate unique string code of 10 digit
class UniqueString():
    id_counter: int = 999

    def __init__(self):
        self.name = self.value()
        UniqueString.id_counter += 1

    def value(self) -> str:
        zerovalue = ['A', 'B', 'C', 'X', 'Y', 'Z']
        mainstr = ""
        count = UniqueString.id_counter
        for i in range(8):
            x = (ord('C') + count % 20)
            count //= 20
            if x == ord('C') or x >= ord('X'):
                mainstr += choice(zerovalue)
            else:
                mainstr += chr(x)
        A, Z = ord('A'), ord('Z')
        mainstr += chr(randint(A, Z))
        mainstr += chr(randint(A, Z))
        return mainstr[::-1]

    def __str__(self) -> str:
        return self.name
