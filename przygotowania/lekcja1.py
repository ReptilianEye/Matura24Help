# print()  # funckja wypisująca na ekran

# typy zmiennych
# zmienne proste
zmienna = 10  # zmienna typu Int
zmienna2 = "Piotrek"  # zmienna typu String
zmienna3 = True  # True/False     Boolean

zmienna4 = 1.2  # Flaot
# print(type(zmienna4))

# lista1 = []
# print(lista1)
# lista1.append(zmienna2)
# print(lista1)
# lista1.append(zmienna)
# print(lista1)
# lista1.insert(0, "pierwszy")
# print(lista1)


#   0     1  21    2   3   4   5
# [ "pie"  x1  x2  x3  x4  x5  x6   ]


# petle
# i = 0
# while i < 10:
#     print(i*3)
#     i += 1  # i = i + 1

# to co sie dzieje w petli

# # cw 1 wypisz 10 pierwszych liczb parzystych
# i = 0
# while i < 10:
#     print(i*2)
#     i += 1  # i = i + 1
# # i = 10

# # cw 2 stworz liste i dodaj do niej 10 pierwszych liczb parzystych
# l = []
# # i = 0
# while i < 10:
#     l.append(i*2)
#     i += 1


# for #zmiennaIterujaca in range(10):
# cialo

# for i in range(10):
#     print(i*3)

# l = [1, 2, 10, 4500, 95]
# for el in l:
#     print(el)

# czyJestDzien = False

# if czyJestDzien:
#     print("jest dzien")
# else:
#     print("jest noc")


a = 1
b = 5
c = 3
# #rozwiazanie 1
# if a > c:
#     if a > b:
#         #a jest najwieksze
#         if b + c > a:
#             print("tak")
#         else:
#             print("nie")
#         pass
#     else:
#         # b > a > c
#         #b jest najwieksze
#         if a + c > b:
#             print("tak")
#         else:
#             print("nie")
#         pass
# else:
#     # a<c
#     if c < b:
#         # a < c < b
#         # b jest najwieksze
#         pass

# rozwiązanie 2
# lista = [a, b, c]
# maksymalnaWartoscWL = max(lista)
# sumaL = sum(lista)
# print(maksymalnaWartoscWL, sumaL)

# sumaL = a + b + c
# maksymalnaWartoscWL = max(a,b,c)

# sume bokow bez maksymalnej wartosci
# print(sumaL-maksymalnaWartoscWL)

# kroki
# znalezc maksymalny bok
# znalezc sume bokow bez maksymalnego boku
# if sprawdzic czy suma bokow bez maksymalny bok > maksymalny bok


def czyDaSieTrojkat(a, b, c, message="Dziala"):  # funkcja z argumentami (a,b,c)
    l = [a, b, c]
    max_v = max(l)
    sum_l = sum(l)
    if sum_l-max_v > max_v:
        # print("Tak")
        return True
    else:
        return False
        # print("Nie")
    print(message)


# argumenty pozycyjne, argumenty nazwowe
response = czyDaSieTrojkat(2, 5, message="bardzo dziala", c=4)
# czyDaSieTrojkat(5, 3, 7)
# print(response)


def zwroc10Kwadrat():  # funkcja bez argumentow
    for i in range(10):
        print("kwadrat")


# code 1
# ....
# zwroc10Kwadrat()
# code 2
# ....

# l = [12, "abc", True, "poker"]
# pierwszyElement = l[1]
# print(pierwszyElement)

# cw 3
# napisać funkcje która sprawdza czy x jest w liście
l = [3, 13, 19, 14, 19, 9, 6, 12, 19, 2, 16, 19, 9, 18, 16, 16, 4, 5, 9, 5]
x = 9


def findX(L, x):
    for el in L:
        if el == x:
            return True
    return False


# findX(l, x)


def findXV2(L, x):
    for index in range(len(L)):
        el = L[index]
        if el == x:
            return index
    return -1


L = ["abc", "def", "hij"]
# for i in range(len(L)):
#     print(L[i])

# print(findXV2(L, "def"))
