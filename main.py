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
        self.grootte = len(raster)
        self.leeg = 0

    def rijen(self):
        for i in range(1,10):
            print(f"rij {i}:\n {self.raster[i-1]}")

    def kolommen(self):
        for i in range(1,10):
            print(f"kolom {i-1}:\n")
            for j in range(1,10):
                kolom = self.raster[j-1][i-1]
                print(f"{kolom}")







    





raadsel = sudoku(puzzle)

raadsel.kolommen()





