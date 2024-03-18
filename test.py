set_sudoku = {}
def oplosser(sudoku):
    # Aanmaak van een niewe dictionary, value wordt hier een lege set. In deze sets komen de nummers in dat door de programma ingevuld is.
    
    for key in sudoku:
        set_sudoku[key] = set()
    # Cellen worden vanaf nu een voor een gecontrolleerd
    prev_waarde = ""
    prev_cel = "A1"
    ingevulde_cellen = []
    for i in range(80):
        for cel,waarde in sudoku.items():
            if waarde == "":
                for num in range(1,10):
                    num = str(num)
                    # Hieronder wordt gecontroleerd of de nummer aanwezig is in de rij,kolom en kamer, indien niet wordt de nummer opgeslaan in de cel.
                    if control_cel(num,cel,func_rij(sudoku),func_kolom(sudoku),func_kamer(sudoku)) and num not in set_sudoku[cel]: 
                        sudoku[cel] = num
                        ingevulde_cellen.append(cel)
                        break # Als de cel ingevuld is stopt de 2de loop, de programma gaat wel verder om de volgende cel te controleren
            if sudoku[cel] == "":
                set_sudoku[prev_cel].add(prev_waarde)
                sudoku[prev_cel] = ""
                #for cellen in ingevulde_cellen:
                #   sudoku[cellen] = ""
                break
            prev_cel = cel
            prev_waarde = num
    print(set_sudoku)


def oplosser(sudoku):
    for num in range(1,10):
        for cel,waarde in sudoku.items():
            if waarde == "":
                if control_cel(num,cel,func_rij(sudoku),func_kolom(sudoku),func_kamer(sudoku)):
                    sudoku[cel]= num
                    if oplosser(sudoku):
                        return True
                    else:
                        sudoku[cel]=""
    return False