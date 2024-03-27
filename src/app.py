from flask import Flask, render_template, request
# import your sudoku solver script
from sudokiller import oplosser, vind_lege_cel, plaats_geldige_nummer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Initialize an empty grid
        grid = [[0 for _ in range(9)] for _ in range(9)]

        # Get the data from the form
        for i in range(9):
            for j in range(9):
                cell = request.form.get(f'cell-{i}-{j}')
                if cell.isdigit():
                    grid[i][j] = int(cell)

        # Solve the sudoku
        oplosser(grid)

        # Convert the grid back to a string
        result = '\n'.join(' '.join(map(str, row)) for row in grid)

        return render_template('index2.html', result=result)

    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
