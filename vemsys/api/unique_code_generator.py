from random import randint, choice


class UniqueCodeGenrator():
    @staticmethod
    def generate(generate_at: int = 0, max_length: int = 10, random_chars: int = 2) -> str:
        zerovalue = ['A', 'B', 'C', 'X', 'Y', 'Z']
        mainstr = ""
        count = generate_at
        for i in range(max_length-random_chars):
            x = (ord('C') + count % 20)
            count //= 20
            if x == ord('C') or x >= ord('X'):
                mainstr += choice(zerovalue)
            else:
                mainstr += chr(x)
        A, Z = ord('A'), ord('Z')
        for i in range(random_chars):
            mainstr += chr(randint(A, Z))
        return mainstr[::-1]

if __name__ == "__main__":
    print( UniqueCodeGenrator().generate(1000) )