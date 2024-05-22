from flask import Flask, render_template, request , session,  redirect, url_for
# import your sudoku solver script
from src.sudokiller import oplosser
from src.Sudoku_game import genereer_sudoku, geldige_sudoku
from src.mijnveger import Minesweeper
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'jouw geheime sleutel'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

"""----------------------------------------Login---------------------------------------------------"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Connectie maken met de database
        db = mysql.connector.connect(
            host = 'localhost',
            user ='root',
            passwd = 'VAP_nam_006',
            database = 'user_data', 
            auth_plugin='mysql_native_password'
        )
        mycursor = db.cursor()

        # Query om de gebruiker op te halen
        mycursor.execute(f"SELECT * FROM user_data WHERE gebruikersnaam = '{username}'")
        user = mycursor.fetchone()

        # Controleer of de gebruiker bestaat en het wachtwoord correct is
        if user and check_password_hash(user[5], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            # Optioneel: foutmelding toevoegen
            pass

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    registration_complete = False
    if request.method == 'POST':
        voornaam = request.form.get('voornaam')
        achternaam = request.form.get('achternaam')
        geboortedatum = request.form.get('geboortedatum')
        username = request.form.get('username')
        password = request.form.get('password')

        # Hash the password before saving it
        hashed_password = generate_password_hash(password)

        # Connect to the database
        db = mysql.connector.connect(
            host = 'localhost',
            user ='root',
            passwd = 'VAP_nam_006',
            database = 'user_data', 
            auth_plugin='mysql_native_password'
        )
        mycursor = db.cursor()

        # Query to save the user
        mycursor.execute(f"INSERT INTO `user_data`.`user_data` (`voornaam`, `achternaam`, `geboortedatum`, `gebruikersnaam`, `password`) VALUES ('{voornaam}', '{achternaam}', '{geboortedatum}', '{username}', '{hashed_password}')")
        db.commit()

        # Set registration_complete to True after successful registration
        registration_complete = True

    return render_template('register.html', registration_complete=registration_complete)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

"""----------------------------------------Sudoku---------------------------------------------------"""
@app.route('/sudoku_oplosser', methods=['GET', 'POST'])
def sudoku_oplosser():
    if 'username' not in session:
        return redirect(url_for('login'))
    grid = [[0 for _ in range(9)] for _ in range(9)]
    user_grid = [[False for _ in range(9)] for _ in range(9)]
    if request.method == 'POST':
        # Get the data from the form
        for i in range(9):
            for j in range(9):
                cell = request.form.get(f'cell-{i}-{j}')
                if cell and cell.isdigit():
                    grid[i][j] = int(cell)
                    user_grid[i][j] = True

        # Solve the sudoku
        oplosser(grid)

    return render_template('sudoku_oplosser.html', grid=grid, user_grid=user_grid)


@app.route('/sudoku_game', methods=['GET', 'POST'])
def sudoku_game():
    grid = [[0]*9 for _ in range(9)]
    user_grid = [[0]*9 for _ in range(9)]
    if request.method == 'POST':
        actie = request.form.get('actie')
        moeilijkheidsgraad = request.form.get('moeilijkheidsgraad')
        if actie == 'nieuw_spel':
            grid = genereer_sudoku(moeilijkheidsgraad)
        elif actie == 'controleer':
            user_grid = []
            for i in range(9):
                rij = []
                for j in range(9):
                    waarde = request.form.get(f'cell-{i}-{j}')
                    if waarde == '':
                        waarde = 0
                    elif waarde.isdigit():
                        waarde = int(waarde)
                    else:
                        abort(400, 'Ongeldige invoer')
                    rij.append(waarde)
                user_grid.append(rij)
            if geldige_sudoku(user_grid):
                return 'Gefeliciteerd, u heeft de sudoku correct opgelost!'
            else:
                return 'Helaas, de sudoku is niet correct opgelost.'
        else:
            abort(400, 'Ongeldige actie')
    return render_template('sudoku.html', grid=grid, user_grid=user_grid)

"""----------------------------------------Minesweeper---------------------------------------------------"""

game = None  # global variable to store the game state

@app.route('/start', methods=['GET', 'POST'])
def start():
    global game
    session['has_won'] = False  # reset the winning status
    if request.method == 'POST':
        difficulty = request.form.get('difficulty')
        game = Minesweeper(difficulty)
    else:
        if game is None:
            game = Minesweeper('makkelijk')  # default to 'makkelijk' difficulty
    return redirect(url_for('mijnveger'))  # always redirect to 'mijnveger'

@app.route('/mijnveger', methods=['GET'])
def mijnveger():
    global game
    if game is None:
        game = Minesweeper('makkelijk')
    return render_template('mijnveger.html', game=game)

@app.route('/reveal', methods=['POST'])
def reveal():
    global game
    row = int(request.form.get('row'))
    col = int(request.form.get('col'))
    result = game.board.reveal_cell(row, col)  # store the output of reveal_cell in result
    if game.board.board[row][col].is_flagged:
        game.board.board[row][col].is_flagged = False
    if result == 'mine':
        game = Minesweeper('makkelijk')  # start a new game with 'makkelijk' difficulty
    elif game.board.has_won():  # check if the game has been won after every reveal
        session['has_won'] = True
    return redirect(url_for('mijnveger'))

@app.route('/flag', methods=['POST'])
def flag():
    global game
    row = int(request.form.get('row'))
    col = int(request.form.get('col'))
    game.board.flag_cell(row, col)
    session['color_grid'] = True  # set color_grid to True
    return redirect(url_for('mijnveger'))

@app.route('/hint', methods=['POST'])
def hint():
    global game
    game.use_hint()
    game.punten -= 1
    return redirect(url_for('mijnveger'))


if __name__ == '__main__':
    app.run(debug=True)

