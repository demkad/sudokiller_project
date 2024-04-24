import random
import time

class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0


class Board:
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]
        self.place_mines()
        self.count_adjacent_mines()


    def place_mines(self):
        mine_positions = random.sample(range(self.size*self.size), self.mines)
        for pos in mine_positions:
            row = pos // self.size
            col = pos % self.size
            self.board[row][col].is_mine = True

    def count_adjacent_mines(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col].is_mine:
                    continue
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= row+dr < self.size and 0 <= col+dc < self.size and self.board[row+dr][col+dc].is_mine:
                            self.board[row][col].adjacent_mines += 1

    def reveal_cell(self, row, col):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            raise ValueError(f"Invalid cell coordinates: ({row}, {col})")
        if self.board[row][col].is_mine:
            return 'mine'
        self.board[row][col].is_revealed = True
        if self.board[row][col].adjacent_mines == 0:
            self.reveal_adjacent_cells(row, col)
        if self.has_won():
            return 'win'
        return ''


    def has_won(self):
        for row in self.board:
            for cell in row:
                if not cell.is_mine and not cell.is_revealed:
                    return False
        return True

    def flag_cell(self, row, col):
        self.board[row][col].is_flagged = not self.board[row][col].is_flagged

    def reveal_adjacent_cells(self, row, col):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < self.size and 0 <= new_col < self.size:
                    cell = self.board[new_row][new_col]
                    if not cell.is_revealed:
                        cell.is_revealed = True
                        cell.is_flagged = False  # reset the flagged status
                        if cell.adjacent_mines == 0:
                            self.reveal_adjacent_cells(new_row, new_col)


class Minesweeper:
    def __init__(self, difficulty):
        if difficulty in ['easy', 'makkelijk']:
            self.board = Board(size=8, mines=10)
        elif difficulty == 'normal':
            self.board = Board(size=16, mines=40)
        elif difficulty == 'hard':
            self.board = Board(size=24, mines=99)
        else:
            raise ValueError(f"Unknown difficulty level: {difficulty}")
        self.start_time = time.time()  # add this line
        self.mines_left = self.board.mines  # add this line
        self.hint_used = False  # add this line

    def use_hint(self):
        for row in range(self.board.size):
            for col in range(self.board.size):
                if not self.board.board[row][col].is_mine and not self.board.board[row][col].is_revealed:
                    self.board.board[row][col].is_revealed = True
                    return

    

    
