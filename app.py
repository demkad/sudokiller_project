from flask import Flask, render_template, request
# import your sudoku solver script
from src.sudokiller import oplosser
from src.Sudoku_game import genereer_sudoku, geldige_sudoku
from werkzeug.exceptions import abort

app = Flask(__name__)
app.secret_key = 'jouw geheime sleutel'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/sudoku_oplosser', methods=['GET', 'POST'])
def sudoku_oplosser():
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


if __name__ == '__main__':
    app.run(debug=True)