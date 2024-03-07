import csv
from prettytable import PrettyTable


# Menus
def menu_user():
    print("1. Toon alle dokters van alle ziekenhuizen")
    print("2. Toon dokters per ziekenhuis")
    print("3. Toon dokter per specialisaie")
    print("4. Sorteer dokters op consultatieprijs") # Duurste eerst
    print("5. Zoek hulp") # Het programma vraagt het ziekenhuis en welke specialisatie
    print("0. Stop")

def menu_admin():
    print("1. Voeg dokter(s) toe") # Vraag aantal dokters
    print("2. Verwijder dokter")
    print("3. Verander specialisatie")
    print("4. Verander consultatieprijs")
    print("5. Update data") # Data wordt opgeslaan in csv
    print("0. Stop")
    
# Inlezen van data   
def lees_csv(file):
    with open(file,"r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = {}
        for row in csv_reader:
            data[row["doktersnaam"]] = {"ziekenhuis": row["ziekenhuis"],"specialisatie": row["specialisatie"],"consultatieprijs": int(row["consultatieprijs"])}
    return data

def dict_user_data(file):
    users = {}
    with open(file, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header
        header = next(reader)
        # Read data and populate the dictionary
        for row in reader:
            user, password = row
            users[user] = password
        return users

# Funcite voor login
def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False


######### Functies USER
def toon_dokters(data):
    myTable = PrettyTable(["Doktersnaam","Ziekenhuis","Specialisatie","Consultatieprijs"])
    rij = []
    for dokter,gegevens in data.items():
        rij.append(dokter)
        rij.append(gegevens["ziekenhuis"])
        rij.append(gegevens["specialisatie"])
        rij.append(gegevens["consultatieprijs"])
        myTable.add_row(rij)
        rij.clear()
    print(myTable)
    
def toon_per_ziekenhuis(data):
    ziekenhuis = input("Vul de ziekenhuis in: ")
    ziekenhuizen = set()
    for dokter,gegevens in data.items():
        ziekenhuizen.add(gegevens["ziekenhuis"]) #Alle voorkomende ziekenhuizen worden toegevoegd in een set
        if ziekenhuis in gegevens.values():
           print(dokter)
    if ziekenhuis not in ziekenhuizen:
        print("Geen dokter gevonden")

def toon_per_specialisatie(data):
    specialisatie = input("Vul de specialisatie in: ")
    specialisaties = set()
    for dokter,gegevens in data.items():
        specialisaties.add(gegevens["specialisatie"]) #Alle voorkomende specialisaties worden toegevoegd in een set
        if specialisatie in gegevens.values():
           print(dokter)
    if specialisatie not in specialisaties:
        print("Geen dokter gevonden")

def sorteer_dokter(data):
    data = dict(sorted(data.items(), key=lambda x: int(x[1]['consultatieprijs']), reverse=True))
    myTable = PrettyTable(["Doktersnaam","Ziekenhuis","Specialisatie","Consultatieprijs"])
    rij = []
    for dokter,gegevens in data.items():
        rij.append(dokter)
        rij.append(gegevens["ziekenhuis"])
        rij.append(gegevens["specialisatie"])
        rij.append(gegevens["consultatieprijs"])
        myTable.add_row(rij)
        rij.clear()
    print(myTable)
    
def zoek_hulp(data):
    ziekenhuis = input("Vul de ziekenhuis in: ")
    specialisatie = input("Vul de specialisatie in: ")
    ziekenhuizen = set()
    specialisaties = set()
    for dokter,gegevens in data.items():
        ziekenhuizen.add(gegevens["ziekenhuis"])
        specialisaties.add(gegevens["specialisatie"])
        if ziekenhuis in gegevens.values() and specialisatie in gegevens.values():
            print(dokter)
    if ziekenhuis not in ziekenhuizen or specialisatie not in specialisaties:
        print("Geen dokter gevonden")
        

###### Functies ADMIN

def voeg_dokter(data):
    aantal = int(input("Hoeveel dokter(s)) wilt u toevoegen: "))
    for i in range(aantal):
        dokter = input(f"Vul de naam van de dokter {i+1} in: ")
        ziekenhuis = input(f"Vul de ziekenhuis van de {dokter} in: ")
        specialisatie = input(f"Vul de specialisatie van de {dokter} in: ")
        consultatieprijs = int(input(f"Vul de consultatieprijs van de {dokter} in: "))
        data[dokter] = {"ziekenhuis":ziekenhuis,"specialisatie":specialisatie,"consultatieprijs":consultatieprijs}
        print(f"{dokter} is toegevoegd!")

def verwijder_dokter(data):
    dokter = input("Welke dokter wilt u verwijderen: ")
    if dokter in data:
        del data[dokter]
        print(f"{dokter} is verwijdert uit de lijst")
    else: print("Dokter niet gevonden")

def verander_specialisatie(data):
    dokter = input("Vul de naam van de dokter in: ")
    if dokter in data:
        nieuw_specialisatie = input(f"Vul de nieuwe specialisatie van {dokter} in: ")
        data[dokter]["specialisatie"] = nieuw_specialisatie
        print(f"Specialisatie van {dokter} is aangepast naar {nieuw_specialisatie}")
    else: print("Dokter niet gevonden")
        
def verander_consultatieprijs(data):
    dokter = input("Vul de naam van de dokter in: ")
    if dokter in data:
        nieuw_consultatieprijs = input(f"Vul de nieuwe consultatieprijs van {dokter} in: ")
        data[dokter]["consultatieprijs"] = nieuw_consultatieprijs
        print(f"Consultatieprijs van {dokter} is aangepast naar {nieuw_consultatieprijs}")
    else: print("Dokter niet gevonden")
    
def update_data(file,data):
    with open(file,"w",newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["doktersnaam","ziekenhuis","specialisatie","consultatieprijs"]) #Titel
        for dokter,gegevens in data.items():
            csv_writer.writerow([dokter,gegevens["ziekenhuis"],gegevens["specialisatie"],gegevens["consultatieprijs"]])
    print("Data is opgeslaan!")
   
##### HP #####
file = "dokters.csv"    #File data
file_user = "users.csv" #File voor login
data = lees_csv(file)
users = dict_user_data(file_user)
functies_user = {"1":toon_dokters,"2":toon_per_ziekenhuis,"3":toon_per_specialisatie,"4":sorteer_dokter,"5":zoek_hulp}
functies_admin = {"1":voeg_dokter,"2":verwijder_dokter,"3":verander_specialisatie,"4":verander_consultatieprijs,"5":update_data}

admin_user = input("Bent u 'user' of 'admin': ")

if admin_user.upper() == "USER":
    if login(users) == True:
        menu_user()
        invoer = input("Kies een functie: ")
        while invoer != "0":
            if invoer in functies_user:
                functies_user[invoer](data)
            menu_user()
            invoer = input("Kies een functie: ")

elif admin_user.upper() == "ADMIN":
    menu_admin()
    invoer = input("Kies een functie: ")
    while invoer != "0":
        if invoer == "5":
            functies_admin[invoer](file,data)
        elif invoer in functies_admin:
            functies_admin[invoer](data)
        menu_admin()
        invoer = input("Kies een functie: ")