import mysql.connector
"""
# Om connectie te maken met mysql workbench moet je de volgende query uitvoeren in mysql workbench.
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'VAP_nam_006';

"""
# Database gegevens. 
# Verander User en passwd door uw eigen mysql workbench gegevens.
# Database moet user_data zijn. 
db = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd = 'VAP_nam_006',
    database = 'user_data', # Database naam, dit moet u verwijderen als u de database nog niet heeft aangemaakt
    auth_plugin='mysql_native_password'
)

mycursor= db.cursor()

# Om uw database aan te maken -> verwijder # aan begin regel 16
# mycursor.execute("CREATE DATABASE user_data")


# Geef uw query in
user_data = """
CREATE TABLE `user_data`.`user_data` (
  `perid` INT NOT NULL AUTO_INCREMENT,
  `Voornaam` VARCHAR(45) NULL,
  `Achternaam` VARCHAR(45) NULL,
  `Geboortedatum` DATE NULL,
  `Gebruikersnaam` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`perid`),
  UNIQUE INDEX `Gebruikersnaam_UNIQUE` (`Gebruikersnaam` ASC) VISIBLE);
"""

sql = user_data

mycursor.execute(sql)

mycursor.close()

db.close()


"""
data gebruiker
- perid (pk)
- voornaam
- achternaam
- geboortedatum
- gebruikersnaam
- password

data game
- spelid (pk)
- naam spel

data scorebord
- score_id (pk)
- perid (fk)
- spelid (fk)
- moeielijkheidsgraad
- score 
- time
- datum
"""

