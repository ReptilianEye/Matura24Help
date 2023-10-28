def wczytajDane():

    tab = []
    plik = "dane.txt"
    # plik = "przyklad.txt"
    with open(plik) as file:
        for line in file:
            line = line.strip()
            line = line.split(" ")
            row = []
            for el in line:
                row.append(int(el))
            tab.append(row)
    return tab


def zad1(tab):
    najwiekszy = -10000000000000000000000000000000000000
    najmniejszy = 10000000000000000000000000000000000000
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            
            if najwiekszy < tab[i][j]:
                najwiekszy = tab[i][j]

            if najmniejszy > tab[i][j]:
                najmniejszy = tab[i][j]

    return najwiekszy, najmniejszy

def czySymetryczny(wiersz):
    lewyWskaznik = 0
    prawyWskaznik = -1 #len(wiersz) - 1
    for k in range(len(wiersz)//2):
        if wiersz[lewyWskaznik] != wiersz[prawyWskaznik]:
            return False
        lewyWskaznik += 1
        prawyWskaznik -= 1
    return True


def zad2(tab):
    liczbaWieszyDoUsuniecia = 0
    for wiersz in tab:
        if not czySymetryczny(wiersz):
            liczbaWieszyDoUsuniecia += 1

    return liczbaWieszyDoUsuniecia

def czySasiedziKontrastuja(tab,i,j):
    if i-1 >= 0 and abs(tab[i][j] - tab[i-1][j]) > 128:
        return True
    if j-1 >= 0 and abs(tab[i][j] - tab[i][j-1]) > 128:
        return True
    if j+1 < len(tab[i]) and abs(tab[i][j] - tab[i][j+1]) > 128:
        return True
    if i+1 < len(tab) and  abs(tab[i][j] - tab[i+1][j]) > 128:
        return True
    
    return False

def zad3(tab):
    licznik = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if czySasiedziKontrastuja(tab,i,j) == True:
                licznik += 1
    
    return licznik

def zad4(tab):
    dlugoscNajwiekszego = -1000000000000
    for i in range(320):
        dlugoscAktualnego = 1
        for j in range(1,200):
            if tab[j][i] == tab[j-1][i]:
                dlugoscAktualnego += 1
            else:
                if dlugoscNajwiekszego < dlugoscAktualnego:
                    dlugoscNajwiekszego = dlugoscAktualnego
                dlugoscAktualnego = 1                
        
        if dlugoscNajwiekszego < dlugoscAktualnego:
            dlugoscNajwiekszego = dlugoscAktualnego
    
    return dlugoscNajwiekszego

tab = wczytajDane()
# print(zad1(tab))
print(zad4(tab))
