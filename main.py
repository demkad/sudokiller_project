# Deze dictionary wordt gebruikt om te testen tijdens het programmeren
"""sudoku = {
    'A1': '', 'B1': '', 'C1': '1', 'D1': '', 'E1': '', 'F1': '', 'G1': '', 'H1': '', 'I1': '',
    'A2': '', 'B2': '', 'C2': '', 'D2': '', 'E2': '', 'F2': '', 'G2': '', 'H2': '', 'I2': '',
    'A3': '', 'B3': '', 'C3': '', 'D3': '', 'E3': '', 'F3': '', 'G3': '', 'H3': '', 'I3': '',
    'A4': '', 'B4': '', 'C4': '', 'D4': '', 'E4': '', 'F4': '', 'G4': '', 'H4': '', 'I4': '',
    'A5': '2', 'B5': '', 'C5': '8', 'D5': '9', 'E5': '', 'F5': '', 'G5': '', 'H5': '', 'I5': '',
    'A6': '', 'B6': '', 'C6': '', 'D6': '', 'E6': '', 'F6': '', 'G6': '', 'H6': '', 'I6': '',
    'A7': '', 'B7': '', 'C7': '', 'D7': '', 'E7': '', 'F7': '', 'G7': '', 'H7': '', 'I7': '',
    'A8': '', 'B8': '', 'C8': '', 'D8': '', 'E8': '', 'F8': '', 'G8': '', 'H8': '', 'I8': '',
    'A9': '', 'B9': '', 'C9': '', 'D9': '', 'E9': '', 'F9': '', 'G9': '', 'H9': '', 'I9': ''
    }"""


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
            sudoku[alfa+digit] = ''
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

set_sudoku = {}
def oplosser(sudoku):
    # Aanmaak van een niewe dictionary, value wordt hier een lege set. In deze sets komen de nummers in dat door de programma ingevuld is.
    
    for key in sudoku:
        set_sudoku[key] = set()
    # Cellen worden vanaf nu een voor een gecontrolleerd
    prev_waarde = ""
    prev_cel = "A1"
    for cel,waarde in sudoku.items():
        if waarde == "":
            for num in range(1,10):
                num = str(num)
                # Hieronder wordt gecontroleerd of de nummer aanwezig is in de rij,kolom en kamer, indien niet wordt de nummer opgeslaan in de cel.
                if control_cel(num,cel,func_rij(sudoku),func_kolom(sudoku),func_kamer(sudoku)) and num not in set_sudoku[cel]: 
                    sudoku[cel] = num
                    break # Als de cel ingevuld is stopt de 2de loop, de programma gaat wel verder om de volgende cel te controleren
        if sudoku[cel] == "":
            set_sudoku[prev_cel].add(prev_waarde)
            sudoku[prev_cel] = ""
            return False
        prev_cel = cel
        prev_waarde = num
                    
    
                
                    

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
    








sudoku = func_sudoku()
kolom = func_kolom(sudoku)
rij = func_rij(sudoku)
kamer = func_kamer(sudoku)
oplosser(sudoku)

print_sudoku(sudoku)