unsolved_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# maak functie om door sudoku te lopen en zoek lege cellen:
def vind_lege_cel(su):
    for i in range(9):
        for j in range(9):
            if su[i][j] == 0: 
                return (i,j)  # geef terug in (rij, kolom)
    return None

# maak functie die controleert of nummer geldig is
def plaats_geldige_nummer(su,pos,num):
        # check rij:
        for i in range(9):
            if num == su[pos[0]][i]:
                return False
        
        # check kolom:
        for i in range(9):
            if num == su[i][pos[1]]:
                return False
            
        # check kamer:
        start_x = (pos[0] // 3) * 3
        start_y = (pos[1] // 3) * 3
        for i in range(3):
            for j in range(3):
                if num == su[start_x+i][start_y+j]:
                    return False
        else: 
            return True
    
def oplosser(su):
    positie = vind_lege_cel(su)
    if not positie:
        print('Sudoku opgelost')
        return True
    else:
        rij, kolom = positie
    
    for num in range(1,10):
        if plaats_geldige_nummer(su,(rij,kolom),num):
            su[rij][kolom] = num

            if oplosser(su):
                return True
            else:
                su[rij][kolom] = 0

    return False

## oplossing

if oplosser(unsolved_sudoku):
    print('Sudoku opgelost')
else:
    print('Sudoku kan niet opgelost worden')

print("-----------------------------------------------")

for rij in unsolved_sudoku:
    print(rij)
