import random

def maak_sudoku():
    basis = 3
    zijde = basis*basis
    nums = list(range(1, zijde + 1))
    bord = [[None]*zijde for _ in range(zijde)]
    for i in range(zijde):
        for j in range(zijde):
            bord[i][j] = (i*basis + i//basis + j) % zijde + 1
    for rij in bord:
        random.shuffle(rij)
    random.shuffle(bord)
    return bord

def verwijder_cellen(bord, moeilijkheidsgraad):
    zijde = len(bord)
    cellen_te_verwijderen = zijde*moeilijkheidsgraad
    for _ in range(cellen_te_verwijderen):
        rij, kolom = random.randint(0, zijde - 1), random.randint(0, zijde - 1)
        while bord[rij][kolom] is None:
            rij, kolom = random.randint(0, zijde - 1), random.randint(0, zijde - 1)
        bord[rij][kolom] = None
    return bord

def genereer_sudoku(moeilijkheidsgraad):
    if moeilijkheidsgraad == 'makkelijk':
        moeilijkheidsgraad = 2
    elif moeilijkheidsgraad == 'normaal':
        moeilijkheidsgraad = 3
    elif moeilijkheidsgraad == 'moeilijk':
        moeilijkheidsgraad = 4
    else:
        print('Ongeldige moeilijkheidsgraad')
        return
    sudoku = maak_sudoku()
    sudoku = verwijder_cellen(sudoku, moeilijkheidsgraad)
    return sudoku

moeilijkheidsgraad = input('Kies een moeilijkheidsgraad (makkelijk, normaal, moeilijk): ')
sudoku = genereer_sudoku(moeilijkheidsgraad)
for rij in sudoku:
    print(rij)