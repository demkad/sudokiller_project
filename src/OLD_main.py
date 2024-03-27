# Deze dictionary wordt gebruikt om te testen tijdens het programmeren
sudoku = {
    'A1': 5, 'B1': 0, 'C1': 0, 'D1': 0, 'E1': 0, 'F1': 0, 'G1': 0, 'H1': 0, 'I1': 9,
    'A2': 0, 'B2': 0, 'C2': 0, 'D2': 0, 'E2': 0, 'F2': 0, 'G2': 0, 'H2': 0, 'I2': 0,
    'A3': 2, 'B3': 0, 'C3': 0, 'D3': 0, 'E3': 0, 'F3': 0, 'G3': 0, 'H3': 0, 'I3': 7,
    'A4': 0, 'B4': 0, 'C4': 0, 'D4': 0, 'E4': 0, 'F4': 0, 'G4': 0, 'H4': 0, 'I4': 0,
    'A5': 0, 'B5': 0, 'C5': 0, 'D5': 0, 'E5': 0, 'F5': 0, 'G5': 0, 'H5': 0, 'I5': 0,
    'A6': 6, 'B6': 0, 'C6': 0, 'D6': 0, 'E6': 0, 'F6': 0, 'G6': 0, 'H6': 0, 'I6': 2,
    'A7': 0, 'B7': 0, 'C7': 0, 'D7': 0, 'E7': 0, 'F7': 0, 'G7': 0, 'H7': 0, 'I7': 0,
    'A8': 9, 'B8': 0, 'C8': 0, 'D8': 0, 'E8': 0, 'F8': 0, 'G8': 0, 'H8': 0, 'I8': 5,
    'A9': 0, 'B9': 0, 'C9': 1, 'D9': 1, 'E9': 3, 'F9': 0, 'G9': 0, 'H9': 0, 'I9': 0
}


"""---------- Sudoku aanmaak en verdelingen per kolom, rij en kamer ----------"""
# invoer = int(input("Kies de maat van u sudoku (4:4x4),(6:6x6),(9:9x9),(12:12x12): "))
# dit later toevoegen in functie func_sudoku(invoer)

# Aanmaken van een lege sudoku
def func_sudoku():
    invoer = 9 # later wordt dit gewijzigd 
    sudoku = {}
    list_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    list_digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10','11','12']
    for digit in list_digit[0:invoer]:
        for alfa in list_alfa[0:invoer]:
            sudoku[alfa+digit] = 0
    return sudoku

# Cellen van sudoku worden verdeeld per kolom
def func_kolom(sudoku):
    kolom = {}
    for i in sudoku:
        if i[1] == "2": # Stopt de programma als alle kolommen overlopen is (voor optimalisatie van de programma)
            break 
        else: 
            var = {}
            for cel,waarde in sudoku.items():
                # Als de letters van de cellen overeenkomen, worden ze in de dict toegevoegd
                if i[0] == cel[0]: 
                    var[cel] = waarde
            kolom[i[0]] = var
    return kolom 
    # Output vb: {'A': {'A1': '', 'A2': '', 'A3': '', 'A4': ''}, 'B': {'B1': '', 'B2': '', 'B3': '', 'B4': ''}}

# Cellen van sudoku worden verdeeld per rij
def func_rij(sudoku):
    rij = {}
    for i in sudoku:
        var = {}
        for cel,waarde in sudoku.items():
            # Als de cijfers van de cellen overeenkomen, worden ze in de dict toegevoegd
            if i[1] == cel[1]:
                var[cel] = waarde
        rij[i[1]] = var
    return rij
    # Output vb: {'1': {'A1': '', 'B1': '', 'C1': '', 'D1': ''}, '2': {'A2': '', 'B2': '', 'C2': '', 'D2': ''}}

# Cellen van sudoku worden verdeeld per kamer
def func_kamer(sudoku):
    kamer = {}
    my_dict = {}
    deel = 3
    list_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    list_digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10','11','12']
    for cel,waarde in sudoku.items():
        index_kolom = list_alfa.index(cel[0])
        index_rij = list_digit.index(cel[1])
        kamer_kolom = index_kolom // deel
        kamer_rij = index_rij // deel
        for i in range(0,deel):
            for x in range(0,deel):
                if (kamer_kolom == x) and (kamer_rij == i):
                    kamer_id = (i*deel)+x
                    if kamer_id in my_dict:
                        my_dict[kamer_id][cel] = waarde
                    else:
                        my_dict[kamer_id] = {cel:waarde}
        # ---- Tot hier zijn de cellen per kamers verdeeld ----
        # vb: {0: {'A1': '', 'B1': '', 'C1': '', 'A2': '', 'B2': '', 'C2': '', 'A3': '', 'B3': '', 'C3': ''}}
    for cel in sudoku:    
        for nest in my_dict.values():
            if cel in nest:
                kamer[cel]=nest
    return kamer
    # Output vb: {'A1': {'A1': '', 'B1': '', 'C1': '', 'A2': '', 'B2': '', 'C2': '', 'A3': '', 'B3': '', 'C3': ''}}

"""---------- Oplossen van de sudoku ----------"""

def control_cel(num,cel,rij,kolom,kamer):
    if num in rij[cel[1]].values() or num in kolom[cel[0]].values() or num in kamer[cel].values():
        return False
    else: 
        return True

def vind_lege_cel(sudoku):
    for cel,waarde in sudoku.items():
        if sudoku[cel] == 0:
            return cel
    return None


set_sudoku = {}
def oplosser(sudoku):
    positie = vind_lege_cel(sudoku)
    if not positie:
        return True
    else:
        cel = positie

    for num in range(1,10):
        if control_cel(num,cel,func_rij(sudoku),func_kolom(sudoku),func_kamer(sudoku)):
            sudoku[cel] = num
            if oplosser(sudoku):
                return True
            else:
                sudoku[cel] = 0
    return False
                    

# voor beter beeld op de sudoku te krijgen
def print_sudoku(grid):
    grid_2d = []
    grid_rij = []
    for cel, waarde in grid.items():
        grid_rij.append(waarde)
        if len(grid_rij) == 9:
            grid_2d.append(grid_rij)
            grid_rij = [] 
    for rij in grid_2d:
        print(rij)

# hans ikke hier ook proberen voor op te lossen met 2D lijst:
"""
def oplosser_k(su):
    # maak 2D lijst van dict:
    grid_2d = []
    grid_rij = []
    for cel, waarde in su.items():
        grid_rij.append(waarde)
        if len(grid_rij) == 9:
            grid_2d.append(grid_rij)
    
    # grid_2d is nu de volledige sudoku in 2d lijst
"""

#sudoku = func_sudoku()
kolom = func_kolom(sudoku)
rij = func_rij(sudoku)
kamer = func_kamer(sudoku)
oplosser(sudoku)

print_sudoku(sudoku)