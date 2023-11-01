import random
import math
def generateFirst(example:bool=False):
    if example:
        file ="dane1przyklad"
        lines = 10
        columns = 20
    else:
        file ="dane1"
        lines = 300
        columns=500  
    with open(file+".txt","w") as file:
        for _ in range(lines):
            filler = random.randint(1,15)
            fillerCount = random.randint(4,math.ceil(math.sqrt(columns)))
            sameFragment = [filler for _ in range(fillerCount)]
            line = []
            for _ in range(columns-fillerCount):
                line.append(random.randint(0,math.ceil(math.sqrt(columns))))
                # line.append(random.randint(0,math.ceil(math.sqrt(columns))))
            index = random.randint(0,len(line))
            line = line[:index] + sameFragment + line[index:]
            line = " ".join([str(i) for i in line]) + "\n"
            file.write(line)


def convert(num:int,base:int=2):
    converted = ""
    while num > 0:
        converted += str(num%base)
        num //= base
    return converted[::-1]

#generated numbers in binary, hex and decimal
def generateSecond(example:bool=False):
    if example:
        file ="dane2przyklad"
        lines = 10
    else:
        file ="dane2"
        lines = 300
    possible = [2,4,8,16]
    with open(file+".txt","w") as file:
        for _ in range(lines):
            pos = random.choice(possible)
            number = random.randint(0,10000)
            line = f"{pos} {convert(number,pos)}\n"
            file.write(line)

generateSecond(True)
generateSecond()