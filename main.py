# github test
su= {
    'A1': '', 'B1': '', 'C1': '', 'D1': '', 'E1': '', 'F1': '', 'G1': '', 'H1': '', 'I1': '',
    'A2': '', 'B2': '', 'C2': '', 'D2': '', 'E2': '', 'F2': '', 'G2': '', 'H2': '', 'I2': '',
    'A3': '', 'B3': '', 'C3': '', 'D3': '', 'E3': '', 'F3': '', 'G3': '', 'H3': '', 'I3': '',
    'A4': '', 'B4': '', 'C4': '', 'D4': '', 'E4': '', 'F4': '', 'G4': '', 'H4': '', 'I4': '',
    'A5': '', 'B5': '', 'C5': '', 'D5': '', 'E5': '', 'F5': '', 'G5': '', 'H5': '', 'I5': '',
    'A6': '', 'B6': '', 'C6': '', 'D6': '', 'E6': '', 'F6': '', 'G6': '', 'H6': '', 'I6': '',
    'A7': '', 'B7': '', 'C7': '', 'D7': '', 'E7': '', 'F7': '', 'G7': '', 'H7': '', 'I7': '',
    'A8': '', 'B8': '', 'C8': '', 'D8': '', 'E8': '', 'F8': '', 'G8': '', 'H8': '', 'I8': '',
    'A9': '', 'B9': '', 'C9': '', 'D9': '', 'E9': '', 'F9': '', 'G9': '', 'H9': '', 'I9': ''
    }

# Invoer 4,6,9,12
#invoer = int(input("Kies de maat van u sudoku (2: 2x2) (9: 9x9): "))
invoer = 9

# Opslag
sudoku= {}
kolom = {}
rij = {}
kamer = {}
list_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10','11','12']

# Aanmaak dict
for digit in list_digit[0:invoer]:
    for alfa in list_alfa[0:invoer]:
        sudoku[alfa+digit] = ''

# Combinaties
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
        # Output: {'A': {'A1': '', 'A2': '', 'A3': '', 'A4': ''}, 'B': {'B1': '', 'B2': '', 'B3': '', 'B4': ''}, 'C': {'C1': '', 'C2': '', 'C3': '', 'C4': ''}, 'D': {'D1': '', 'D2': '', 'D3': '', 'D4': ''}}

for i in sudoku:
    var = {}
    for cel,waarde in sudoku.items():
        # Als de cijfers van de cellen overeenkomen, worden ze in de dict toegevoegd
        if i[1] == cel[1]:
            var[cel] = waarde
    rij[i[1]] = var
    # Output: {'1': {'A1': '', 'B1': '', 'C1': '', 'D1': ''}, '2': {'A2': '', 'B2': '', 'C2': '', 'D2': ''}, '3': {'A3': '', 'B3': '', 'C3': '', 'D3': ''}, '4': {'A4': '', 'B4': '', 'C4': '', 'D4': ''}}




var = {}
for cel,waarde in sudoku.items():
    index_kolom = list_alfa.index(cel[0])
    index_rij = list_digit.index(cel[1])
    kamer_kolom = index_kolom // 3
    kamer_rij = index_rij // 3
    for i in range(0,3):
        for x in range(0,3):
            if (kamer_kolom == x) and (kamer_rij == i):
                kamer = (i*3)+x
                print(cel,kamer)




    # print(f"cel: {cel} \nrij: {index_rij,kamer_rij} \nkolom: {index_kolom,kamer_kolom}")


"""for i in su:
    var = {}
    for cel,waarde in su.items():
        if i[0] == cel[0]:
            var[cel] = waarde
    combinatie_v[i] = var

for i in su:
    var = {}
    for cel,waarde in su.items():
        if i[1] == cel[1]:
            var[cel] = waarde
    combinatie_h[i] = var
"""