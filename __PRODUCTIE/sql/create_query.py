import mysql.connector


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
sql = """
CREATE TABLE `user_data`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
"""

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

