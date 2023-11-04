# zadania do dane2.txt


def readInput():
    dane = []
    filename = "dane2.txt"
    # filename = "dane2przyklad.txt"
    with open(filename, "r") as file:
        for line in file:
            line = line.strip().split(" ")
            dane.append((int(line[0]), line[1]))
    return dane


dane = readInput()
fromHexToDec = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


def fromSystemToDec(system: int, num: str):
    decNum = 0
    num = num[::-1]  # odwróć w miejscu "kot"[::-1] = "tok"
    for i in range(len(num)):
        if num[i] in fromHexToDec:
            decNum += fromHexToDec[num[i]] * system**i
        else:
            decNum += int(num[i]) * system**i
    return decNum


def zad1(dane):
    biggest = -100000000000
    smallest = 100000000000
    for pair in dane:
        decNum = fromSystemToDec(pair[0], pair[1])  # fromSystemToDec(*pair)
        if decNum > biggest:
            biggest = decNum
        if decNum < smallest:
            smallest = decNum
    return biggest, smallest


print(zad1(dane))


def zad2(dane):
    systems = {}
    for pair in dane:
        system = pair[0]
        if system in systems:
            systems[system] += 1
        else:
            systems[system] = 1

    mostNumberous = -1
    mostNumberousSystem = -1
    for system in systems:
        if systems[system] > mostNumberous:
            mostNumberous = systems[system]
            mostNumberousSystem = system
    return mostNumberous, mostNumberousSystem


print(zad2(dane))


def zad3(dane):
    summ = 0
    for pair in dane:
        if pair[0] == 2:
            summ += fromSystemToDec(2, pair[1])

    return bin(summ)[2:]


print(zad3(dane))


def isMoreZerosThanOnes(binNum):
    ones = 0
    zeros = 0
    for digit in binNum:
        if digit == "1":
            ones += 1
        else:
            zeros += 1
    return zeros > ones


def zad4(dane):
    counter = 0
    for pair in dane:
        decNum = fromSystemToDec(pair[0], pair[1])
        if isMoreZerosThanOnes(bin(decNum)[2:]):
            counter += 1
    return counter


print(zad4(dane))


def ifPalindrome(num: str):
    return num == num[::-1]


def zad5(dane):
    counter = 0
    for pair in dane:
        if ifPalindrome(pair[1]):
            counter += 1
    return counter


print(zad5(dane))


def zad6(dane):
    longest = {}
    for pair in dane:
        if pair[0] not in longest:
            longest[pair[0]] = len(pair[1])
        else:
            longest[pair[0]] = max(longest[pair[0]], len(pair[1]))
    for sys in sorted(longest.keys()):
        print(sys, longest[sys])
    # return longest


zad6(dane)
