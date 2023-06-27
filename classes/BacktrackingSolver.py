class BacktrackingSolver:
    def __init__(self, board):
        self.board = board
        self.count = 0

    def find_empty(self):
        for row, row_values in enumerate(self.board):
            for col, value in enumerate(row_values):
                if value == 0:
                    return (row, col)
        return None

    def is_possible(self, num, pos):
        row, col = pos
        # Vérification des doublons dans la ligne
        for c in range(9):
            if self.board[row][c] == num and col != c:
                return False

        # Vérification des doublons dans la colonne
        for r in range(9):
            if self.board[r][col] == num and row != r:
                return False

        # Vérification des doublons dans le carré 3x3
        box_row = row // 3
        box_col = col // 3
        for r in range(box_row * 3, box_row * 3 + 3):
            for c in range(box_col * 3, box_col * 3 + 3):
                if self.board[r][c] == num and (r, c) != pos:
                    return False
        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
        for num in range(1, 10):
            if self.is_possible(num, (row, col)):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False
