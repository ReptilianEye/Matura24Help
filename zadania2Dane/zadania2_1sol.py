# zadania do dane1.txt

from math import sqrt


def readInput():
    dane = []
    filename = "dane1.txt"
    # filename = "dane1przyklad.txt"
    with open(filename, "r") as file:
        for line in file:
            line = line.strip().split(" ")
            line = [int(x) for x in line]
            dane.append(line)
    return dane


def zad1(dane):
    largest = -1000000000
    smallest = 1000000000
    for line in dane:
        for num in line:
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num
    numberOfLargest = 0
    for line in dane:
        for num in line:
            if num == largest:
                numberOfLargest += 1
    numberOfSmallest = 0
    for line in dane:
        for num in line:
            if num == smallest:
                numberOfSmallest += 1
    return largest, numberOfLargest, smallest, numberOfSmallest


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

# verifying isPrime

# for i in range(100):
#     if isPrime(i):
#         print(i, end=" ")


def zad2(dane):
    primesNum = 0
    biggestPrime = -1000000000
    for line in dane:
        for num in line:
            if isPrime(num):
                primesNum += 1
                if num > biggestPrime:
                    biggestPrime = num
    return primesNum, biggestPrime


def zad3(dane):
    longestSeq = 1
    longestSeqNum = dane[0][0]
    for row in dane:
        seq = 1
        for i in range(1, len(row)):
            if row[i] == row[i-1]:
                seq += 1
            else:
                if seq > longestSeq:
                    longestSeq = seq
                    longestSeqNum = row[i-1]
                seq = 1
        if seq > longestSeq:
            longestSeq = seq
            longestSeqNum = row[i-1]

    return longestSeq, longestSeqNum


def zad4(dane):
    longestSeq = 1
    longestSeqNum = dane[0][0]
    for col_index in range(len(dane[0])):
        seq = 1
        for row_index in range(1, len(dane)):
            if dane[row_index][col_index] == dane[row_index-1][col_index]:
                seq += 1
            else:
                if seq > longestSeq:
                    longestSeq = seq
                    longestSeqNum = dane[row_index-1][col_index]
                seq = 1
        if seq > longestSeq:
            longestSeq = seq
            longestSeqNum = dane[row_index-1][col_index]
    return longestSeq, longestSeqNum


def zad5(dane):
    longestSeq = 1
    longestSeqStart = dane[0][0]
    for row in dane:
        seq = 1
        currentStart = row[0]
        for i in range(1, len(row)):
            if row[i] > row[i-1]:
                seq += 1
            else:
                if seq > longestSeq:
                    longestSeq = seq
                    longestSeqStart = currentStart
                seq = 1
                currentStart = row[i]

        if seq > longestSeq:
            longestSeq = seq
            longestSeqStart = currentStart

    return longestSeq, longestSeqStart


def zad6(dane):
    longestSeq = 1
    longestSeqStart = dane[0][0]
    for col in range(len(dane[0])):
        seq = 1
        currentStart = dane[0][col]
        for row in range(1, len(dane)):
            if dane[row][col] > dane[row-1][col]:
                seq += 1
            else:
                if seq > longestSeq:
                    longestSeq = seq
                    longestSeqStart = currentStart
                seq = 1
                currentStart = dane[row][col]
        if seq > longestSeq:
            longestSeq = seq
            longestSeqStart = currentStart
    return longestSeq, longestSeqStart


def zad7(dane):
    elements = []
    for row in dane:
        for num in row:
            if num not in elements:
                elements.append(num)
    return len(set(elements))


def zad8(dane):
    elements = {}
    for row in dane:
        for num in row:
            if num not in elements:
                elements[num] = 1
            else:
                elements[num] += 1
    onlyOnce = 0
    for key in elements:
        if elements[key] == 1:
            onlyOnce += 1
    return onlyOnce


dane = readInput()
# print(zad1(dane))
# print(zad2(dane))
# print(zad3(dane))
# print(zad4(dane))
# print(zad5(dane))
# print(zad6(dane))
# print(zad7(dane))
# print(zad8(dane))
