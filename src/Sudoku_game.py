import random

def maak_sudoku():
    zijde = 9
    bord = [[None]*zijde for _ in range(zijde)]
    for i in range(zijde):
        for j in range(zijde):
            bord[i][j] = (i*3 + i//3 + j) % zijde + 1
    random.shuffle(bord)
    return bord

def is_geldig(bord, rij, kolom, num):
    for x in range(9):
        if bord[rij][x] == num:
            return False

    for x in range(9):
        if bord[x][kolom] == num:
            return False

    startRij = rij - rij % 3
    startKolom = kolom - kolom % 3
    for i in range(3):
        for j in range(3):
            if bord[i + startRij][j + startKolom] == num:
                return False
    return True

def verwijder_cellen(bord, moeilijkheidsgraad):
    zijde = len(bord)
    cellen_te_verwijderen = zijde*moeilijkheidsgraad
    for _ in range(cellen_te_verwijderen):
        rij, kolom = random.randint(0, zijde - 1), random.randint(0, zijde - 1)
        while bord[rij][kolom] is None:
            rij, kolom = random.randint(0, zijde - 1), random.randint(0, zijde - 1)
        bord[rij][kolom] = None
    return bord

def vul_bord(bord, rij=0, kolom=0):
    if rij == 9 - 1 and kolom == 9:
        return True

    if kolom == 9:
        rij += 1
        kolom = 0

    if bord[rij][kolom] is not None and bord[rij][kolom] > 0:
        return vul_bord(bord, rij, kolom + 1)

    for num in range(1, 10):
        if is_geldig(bord, rij, kolom, num):
            bord[rij][kolom] = num

            if vul_bord(bord, rij, kolom + 1):
                return True

        bord[rij][kolom] = None

    return False

def controleer_bord(bord):
    for i in range(9):
        for j in range(9):
            if bord[i][j] is not None:
                temp = bord[i][j]
                bord[i][j] = None
                if not is_geldig(bord, i, j, temp):
                    return False
                bord[i][j] = temp
    return True

def genereer_sudoku(moeilijkheidsgraad):
    bord = [[None for _ in range(9)] for _ in range(9)]
    vul_bord(bord)
    bord = verwijder_cellen(bord, moeilijkheidsgraad)
    return bord
