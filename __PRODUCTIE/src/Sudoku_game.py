import random, time

def geldige_zet(bord, rij, kolom, num):
    rij_blok, kolom_blok = rij - rij % 3, kolom - kolom % 3
    if all(num != bord[i][kolom] for i in range(9)) and all(num != bord[rij][j] for j in range(9)) and all(num != bord[i][j] for i in range(rij_blok, rij_blok + 3) for j in range(kolom_blok, kolom_blok + 3)):
        return True
    return False

def maak_sudoku(bord, rij=0, kolom=0):
    if kolom == 9:
        if rij == 8:
            return True
        rij += 1
        kolom = 0
    if bord[rij][kolom] != 0:
        return maak_sudoku(bord, rij, kolom + 1)
    for num in random.sample(range(1, 10), 9):
        if geldige_zet(bord, rij, kolom, num):
            bord[rij][kolom] = num
            if maak_sudoku(bord, rij, kolom + 1):
                return True
    bord[rij][kolom] = 0
    return False

def genereer_sudoku(moeilijkheidsgraad):
    bord = [[0]*9 for _ in range(9)]
    nummers = random.sample(range(1, 10), 9)
    for i in range(9):
        bord[i][i] = nummers[i]
    maak_sudoku(bord)
    if moeilijkheidsgraad == 'makkelijk':
        leegte = 2
    elif moeilijkheidsgraad == 'normaal':
        leegte = 40
    elif moeilijkheidsgraad == 'moeilijk':
        leegte = 60
    else:
        print('Ongeldige moeilijkheidsgraad')
        return
    cellen = [(i, j) for i in range(9) for j in range(9)]
    for _ in range(leegte):
        i, j = random.choice(cellen)
        cellen.remove((i, j))
        bord[i][j] = 0
    return bord

def geldige_sudoku(bord):
    for i in range(9):
        rij = bord[i]
        if len(set(rij)) != 9 or 0 in rij:
            return False
        kolom = [bord[j][i] for j in range(9)]
        if len(set(kolom)) != 9 or 0 in kolom:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            vierkant = []
            for x in range(3):
                for y in range(3):
                    vierkant.append(bord[i+x][j+y])
            if len(set(vierkant)) != 9 or 0 in vierkant:
                return False
    return True

