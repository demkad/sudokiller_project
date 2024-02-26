## Created by Kadir & Yavuz ##
## Script to solve a Suduku Puzzle ## 

# create unsolved sudoku puzzle to work with #
puzzle = [
    [0,0,0,5,7,0,4,0,0],
    [0,0,0,1,0,8,3,0,5],
    [0,0,0,3,0,0,0,1,7],
    [5,0,0,0,1,6,0,0,0],
    [9,6,0,0,0,0,0,8,4],
    [0,0,0,0,9,0,0,0,6],
    [6,1,0,0,8,4,0,0,0],
    [2,0,8,6,0,0,0,0,1],
    [0,0,3,0,2,1,0,0,0]
]

class sudoku:
    def __init__(self,raster):
        self.raster = raster
    
    def toon_raster(self):
        for rij in self.raster:
            print(rij)
    




# Playground
raadsel = sudoku(puzzle)

raadsel.toon_raster()
