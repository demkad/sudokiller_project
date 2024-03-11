# Su is een voorbeeld
sudoku= {
    'A1': '', 'B1': '', 'C1': '1', 'D1': '', 'E1': '', 'F1': '', 'G1': '', 'H1': '', 'I1': '',
    'A2': '', 'B2': '', 'C2': '', 'D2': '', 'E2': '', 'F2': '', 'G2': '', 'H2': '', 'I2': '',
    'A3': '', 'B3': '', 'C3': '', 'D3': '', 'E3': '', 'F3': '', 'G3': '', 'H3': '', 'I3': '',
    'A4': '', 'B4': '', 'C4': '', 'D4': '', 'E4': '', 'F4': '', 'G4': '', 'H4': '', 'I4': '',
    'A5': '2', 'B5': '', 'C5': '8', 'D5': '9', 'E5': '', 'F5': '', 'G5': '', 'H5': '', 'I5': '',
    'A6': '', 'B6': '', 'C6': '', 'D6': '', 'E6': '', 'F6': '', 'G6': '', 'H6': '', 'I6': '',
    'A7': '', 'B7': '', 'C7': '', 'D7': '', 'E7': '', 'F7': '', 'G7': '', 'H7': '', 'I7': '',
    'A8': '', 'B8': '', 'C8': '', 'D8': '', 'E8': '', 'F8': '', 'G8': '', 'H8': '', 'I8': '',
    'A9': '', 'B9': '', 'C9': '', 'D9': '', 'E9': '', 'F9': '', 'G9': '', 'H9': '', 'I9': ''
    }


#invoer = int(input("Kies de maat van u sudoku (4:4x4),(6:6x6),(9:9x9),(12:12x12): "))
invoer = 9

# Opslag
su= {}
kolom = {}
rij = {}
kamer = {}
list_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10','11','12']

# Aanmaak dict
for digit in list_digit[0:invoer]:
    for alfa in list_alfa[0:invoer]:
        su[alfa+digit] = ''

# Aanmaak kolommen,rijen en kamers per cel
# Aanmaak kolom
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
# Aanmaak rij
for i in sudoku:
    var = {}
    for cel,waarde in sudoku.items():
        # Als de cijfers van de cellen overeenkomen, worden ze in de dict toegevoegd
        if i[1] == cel[1]:
            var[cel] = waarde
    rij[i[1]] = var
    # Output: {'1': {'A1': '', 'B1': '', 'C1': '', 'D1': ''}, '2': {'A2': '', 'B2': '', 'C2': '', 'D2': ''}, '3': {'A3': '', 'B3': '', 'C3': '', 'D3': ''}, '4': {'A4': '', 'B4': '', 'C4': '', 'D4': ''}}
# Aanmaak kamers
my_dict = {}
deel = 3
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
    # ---- Tot hier zijn de wellen per kamers verdeeld ----
for cel in sudoku:    
    for nest in my_dict.values():
        if cel in nest:
            kamer[cel]=nest 



# OPLOSSEN


def control_cel(num,functie_cel):
    if num in rij[functie_cel[1]].values() or num in kolom[functie_cel[0]].values() or num in kamer[functie_cel].values():
        return False
    else: 
        return True


def oplosser():
    for cel,waarde in sudoku.items():
        if waarde == "":
            for i in range(1,10):
                i = str(i)
                if control_cel(i,cel):
                    sudoku[cel] = i
                    break



## voor beter beeld op de sudoku te krijgen
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



print("noob")
        

        

oplosser()
print_sudoku(sudoku)
                






"""for cel,waarde in sudoku.items():
    if waarde == "":
        for i in range(1,invoer+1):
            i = str(i)
            if i in rij[cel[1]].values() or i in kolom[cel[0]].values() or i in kamer[cel].values():
                None
            else: sudoku[cel] = i

for cel,waarde in sudoku.items():
    if cel[1] == '5':
        print(cel,waarde)"""

"""print(rij["1"])
print(kamer['A5'])
print(kolom["B"])"""