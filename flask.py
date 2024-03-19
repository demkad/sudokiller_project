from flask import Flask, render_template, request
# import your sudoku solver script
from main_2 import oplosser, vind_lege_cel, plaats_geldige_nummer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the data from the form
        grid = request.form.get('grid')

        # Convert the grid to a 2D list
        grid = [list(map(int, row.split())) for row in grid.split('\n')]

        # Solve the sudoku
        result = oplosser(grid)

        # Convert the result back to a string
        result = '\n'.join(' '.join(map(str, row)) for row in result)

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
