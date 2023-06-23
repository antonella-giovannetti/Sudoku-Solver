from classes.BacktrackingSolver import BacktrackingSolver
import pygame

def file_to_list(file_path):
    with open(file_path, 'r') as file:
        content_file = file.readlines()
        res = []
        for line in content_file:
            clean_line = line.replace("_", '0').replace('\n', '')
            list_numbers = list(map(int, clean_line))
            res.append(list_numbers)
    return res

sudoku_files = ["grid/sudoku.txt", "grid/sudoku2.txt", "grid/sudoku3.txt", "grid/sudoku4.txt", "grid/evilsudoku.txt"]

for file_path in sudoku_files:  
    sudoku_board = file_to_list(file_path)
    sudoku_solver = BacktrackingSolver(sudoku_board)
    print(' ')
    print('Initial board:')
    sudoku_solver.print_board()
    print('Resolution:')
    sudoku_solver.solve()
    sudoku_solver.print_board()
    print(' ')



