from flask import Flask, flash, render_template, request
# import your sudoku solver script
from src.sudokiller import oplosser, vind_lege_cel, plaats_geldige_nummer
from src.Sudoku_game import genereer_sudoku,controleer_bord

app = Flask(__name__)
app.secret_key = 'jouw geheime sleutel'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/sudoku', methods=['GET', 'POST'])
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

    return render_template('index2.html', grid=grid, user_grid=user_grid)


@app.route('/sudoku_game', methods=['GET', 'POST'])
def sudoku_game():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    user_grid = [[False for _ in range(9)] for _ in range(9)]
    if request.method == 'POST':
        if request.form.get('submit') == 'Nieuwe Spel':
            # Get the difficulty from the form
            difficulty = request.form.get('difficulty')
            # Convert the difficulty to an integer
            difficulty_dict = {'makkelijk': 1, 'normaal': 2, 'moeilijk': 3}
            difficulty = difficulty_dict.get(difficulty, 1)
            # Generate the Sudoku game
            grid = genereer_sudoku(difficulty)
            for i in range(9):
                for j in range(9):
                    if grid[i][j] is not None:
                        user_grid[i][j] = True
        elif request.form.get('submit') == 'Check':
            # Get the data from the form
            for i in range(9):
                for j in range(9):
                    cell = request.form.get(f'cell-{i}-{j}')
                    if cell and cell.isdigit():
                        grid[i][j] = int(cell)
                        user_grid[i][j] = True
            # Check the sudoku
            if controleer_bord(grid):
                flash('Correct opgelost!')
            else:
                flash('Fout opgelost!')

    return render_template('sudoku.html', grid=grid, user_grid=user_grid)


if __name__ == '__main__':
    app.run(debug=True)