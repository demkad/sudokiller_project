document.addEventListener('DOMContentLoaded', function() {
    const sudokuContainer = document.querySelector('.sudoku-container');
    const generateBtn = document.getElementById('generate-btn');
    const solveBtn = document.getElementById('solve-btn');
    const hintBtn = document.getElementById('hint-btn');

    // Function to generate the Sudoku grid
    function generateSudokuGrid(sudokuArray) {
        sudokuContainer.innerHTML = '';
        sudokuArray.forEach((row, rowIndex) => {
            row.forEach((cell, cellIndex) => {
                const cellDiv = document.createElement('div');
                cellDiv.classList.add('sudoku-cell');
                cellDiv.textContent = cell === 0 ? '' : cell;
                sudokuContainer.appendChild(cellDiv);
            });
        });
    }

    // Function to fetch a new Sudoku puzzle from the server
    async function generateSudoku() {
        try {
            const response = await fetch('/generate_sudoku');
            if (!response.ok) {
                throw new Error('Failed to generate Sudoku puzzle');
            }
            const data = await response.json();
            generateSudokuGrid(data.sudoku_grid);
        } catch (error) {
            console.error(error);
            alert('Failed to generate Sudoku puzzle');
        }
    }

    // Function to solve the Sudoku puzzle
    async function solveSudoku() {
        const sudokuGrid = getSudokuGridValues();
        try {
            const response = await fetch('/solve_sudoku', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ sudoku_grid: sudokuGrid })
            });
            if (!response.ok) {
                throw new Error('Failed to solve Sudoku puzzle');
            }
            const data = await response.json();
            generateSudokuGrid(data.solved_grid);
        } catch (error) {
            console.error(error);
            alert('Failed to solve Sudoku puzzle');
        }
    }

    // Function to get the current Sudoku grid values
    function getSudokuGridValues() {
        const sudokuCells = sudokuContainer.querySelectorAll('.sudoku-cell');
        const sudokuGrid = [];
        sudokuCells.forEach(cell => {
            sudokuGrid.push(parseInt(cell.textContent) || 0);
        });
        return sudokuGrid;
    }

    // Event listeners for button clicks
    generateBtn.addEventListener('click', generateSudoku);
    solveBtn.addEventListener('click', solveSudoku);
});
