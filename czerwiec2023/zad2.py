# 2.1
# s = assssssst
# k1 = 1
# k2 = 2

with open(r"dane\slowa3.txt") as file:
    n = int(file.readline().strip())
    s = file.readline().strip()
    k1, k2 = map(int, file.readline().strip().split())
# print(n, s, k1, k2)


def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    while i < n and j < n:
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return True
            else:
                return False
    if j < n:
        return True
    else:
        return False


# print(czy_mniejszy(n, s, k1-1, k2-1))

# zad 2.3
def genT(n, s):
    # Temp = [s[i:n] for i in range(n)]
    T = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if czy_mniejszy(n, s, T[i], T[j]):
                T[i], T[j] = T[j], T[i]
    T = [T[i] + 1 for i in range(n)]
    print(T)


# genT(10, "mascarpone")


def findLowest(n, s):
    # n = len(s)
    lowest_idx = 0
    for i in range(n):
        if not czy_mniejszy(n, s, lowest_idx, i):
            lowest_idx = i
        s1 = s[i:n]
    return s[lowest_idx:n]

# zad 2.4


def solve24(dane=r'dane\slowa4.txt'):

    with open(dane) as file:
        for line in file:
            n, s = line.strip().split()
            n = int(n)
            print(findLowest(n, s))


# solve24()

# zad 3.1


def count10(bnumber):
    count0 = 0
    count1 = 0
    for i in bnumber:
        if i == "0":
            count0 += 1
        else:
            count1 += 1
    return count0, count1


def zad31():
    # dane = r'dane\przyklad.txt'
    dane = r'dane\anagram.txt'
    zrownowazone = 0
    prawieZrownowazone = 0
    with open(dane) as file:
        for line in file:
            bnumber = line.strip()
            count0, count1 = count10(bnumber)
            if count0 == count1:
                zrownowazone += 1
            elif abs(count0-count1) == 1:
                prawieZrownowazone += 1
    print(zrownowazone)
    print(prawieZrownowazone)


# zad31()

# zad 3.2
def zad32():
    dane = r'dane\anagram.txt'
    with open(dane) as file:
        for line in file:
            bnumber = line.strip()
            if len(bnumber) == 8:
                count0, count1 = count10(bnumber)
                if count1 in [4, 5]:
                    print(bnumber)


# zad32()


# zad 3.3
def toBinary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def fromBinary(binary):
    n = 0
    for i in range(len(binary)):
        n += int(binary[i]) * 2 ** (len(binary) - i - 1)
    return n


def zad33():
    binaries = []
    dane = r'dane\anagram.txt'
    # dane = r'dane\przyklad.txt'
    with open(dane) as file:
        for line in file:
            bnumber = line.strip()
            binaries.append(bnumber)
    maxDiff = -1
    for i in range(len(binaries)-1):
        diff = abs(fromBinary(binaries[i]) - fromBinary(binaries[i+1]))
        if maxDiff < diff:
            maxDiff = diff
    print(toBinary(maxDiff))


# zad33()

# zad 3.4
def splitNumber(num):
    digits = [False for _ in range(10)]
    if num == 0:
        digits[0] = True
        return
    while num > 0:
        digits[num % 10] = True
        num //= 10
    return digits


def sumDistinctDigits(digits):
    sum = 0
    for i in range(10):
        if digits[i]:
            sum += i
    return sum


def zad34():
    hasNoZero = 0
    biggestSum = 0
    biggestSumNumber = 0
    dane = r'dane\anagram.txt'
    # dane = r'dane\przyklad.txt'
    with open(dane) as file:
        for line in file:
            bnumber = line.strip()
            digits = splitNumber(fromBinary(bnumber))
            if not digits[0]:
                hasNoZero += 1
            sum = sumDistinctDigits(digits)
            if biggestSum < sum:
                biggestSum = sum
                biggestSumNumber = fromBinary(bnumber)
    print(hasNoZero)
    print(biggestSumNumber)


zad34()
