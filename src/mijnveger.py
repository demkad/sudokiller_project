import random
import time

class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0

    def to_dict(self):
        return {
            'is_mine': self.is_mine,
            'is_revealed': self.is_revealed,
            'is_flagged': self.is_flagged,
            'adjacent_mines': self.adjacent_mines,
        }

    @classmethod
    def from_dict(cls, data):
        cell = cls()
        cell.is_mine = data['is_mine']
        cell.is_revealed = data['is_revealed']
        cell.is_flagged = data['is_flagged']
        cell.adjacent_mines = data['adjacent_mines']
        return cell

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



import time

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
        if not self.hint_used:
            self.hint_used = True
            self.start_time -= 600
            for row in range(self.board.size):
                for col in range(self.board.size):
                    if self.board.board[row][col].is_mine:
                        return (row, col)

    def is_game_over(self):
        for row in range(self.board.size):
            for col in range(self.board.size):
                if self.board.board[row][col].is_exploded or (not self.board.board[row][col].is_mine and not self.board.board[row][col].is_revealed):
                    return False
        return True

    def is_game_won(self):
        return self.is_game_over() and not any(cell.is_exploded for row in self.board.board for cell in row)
    
    def to_dict(self):
        return {
            'board': [[cell.to_dict() for cell in row] for row in self.board.board],
            'start_time': self.start_time,
            'mines_left': self.mines_left,
            'hint_used': self.hint_used,
        }

    @classmethod
    def from_dict(cls, data):
        game = cls('makkelijk')  # moeilijkheidsgraad doet er niet toe omdat we het bord overschrijven
        game.board.board = [[Cell.from_dict(cell_data) for cell_data in row] for row in data['board']]
        game.start_time = data['start_time']
        game.mines_left = data['mines_left']
        game.hint_used = data['hint_used']
        return game    
    
def main():
    difficulty = input('Kies een moeilijkheidsgraad (makkelijk, normaal, moeilijk): ')
    game = Minesweeper(difficulty)

    while not game.is_game_over():
        action = input('Voer een actie in (reveal, flag, hint): ')
        if action == 'reveal':
            row = int(input('Voer de rij in: '))
            col = int(input('Voer de kolom in: '))
            game.board.reveal_cell(row, col)
        elif action == 'flag':
            row = int(input('Voer de rij in: '))
            col = int(input('Voer de kolom in: '))
            game.board.flag_cell(row, col)
        elif action == 'hint':
            hint = game.use_hint()
            print(f'Hint: er is een mijn op positie ({hint[0]}, {hint[1]})')
    if game.is_game_won():
        print('Gefeliciteerd, je hebt gewonnen!')
    else:
        print('Helaas, je hebt verloren.')
    # Hier zou je de game loop implementeren waar de gebruiker acties kan uitvoeren zoals het onthullen van een cel, het plaatsen van een vlag, of het gebruiken van een hint.