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
  `voornaam` VARCHAR(45) NULL,
  `achternaam` VARCHAR(45) NULL,
  `geboortedatum` DATE NULL,
  `gebruikersnaam` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`perid`),
  UNIQUE INDEX `gebruikersnaam_UNIQUE` (`gebruikersnaam` ASC) VISIBLE);
"""
games_data = """
CREATE TABLE `user_data`.`games_data` (
  `game_id` INT NOT NULL AUTO_INCREMENT,
  `naam` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Game_id`));
"""

scorebord_data = """
CREATE TABLE `user_data`.`scorebord_data` (
  `score_id` INT NOT NULL AUTO_INCREMENT,
  `perid` INT NOT NULL,
  `game_id` INT NOT NULL,
  `moeielijkheidsgraad` VARCHAR(45) NULL,
  `score` INT NOT NULL,
  `tijd` VARCHAR(45) NULL,
  `datum` DATE NULL,
  PRIMARY KEY (`score_id`),
  INDEX `user_idx` (`perid` ASC) VISIBLE,
  INDEX `game_idx` (`game_id` ASC) VISIBLE,
  CONSTRAINT `user`
    FOREIGN KEY (`perid`)
    REFERENCES `user_data`.`user_data` (`perid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `game`
    FOREIGN KEY (`game_id`)
    REFERENCES `user_data`.`games_data` (`game_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
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
- game_id (pk)
- naam spel

data scorebord
- score_id (pk)
- perid (fk)
- game_id (fk)
- moeielijkheidsgraad
- score 
- tijd
- datum
"""

