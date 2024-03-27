from flask import Flask, render_template, request
# import your sudoku solver script
from src.sudokiller import oplosser, vind_lege_cel, plaats_geldige_nummer

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)