from classes.BacktrackingSolver import BacktrackingSolver
from classes.BruteforceSolver import BruteforceSolver
import pygame
import pygame.key
from pygame.locals import *
import sys

def file_to_list(file_path):
    with open(file_path, 'r') as file:
        content_file = file.readlines()
        res = []
        for line in content_file:
            clean_line = line.replace("_", '0').replace('\n', '')
            list_numbers = list(map(int, clean_line))
            res.append(list_numbers)
    return res

def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - - ")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")

sudoku_files = ["grid/sudoku.txt", "grid/sudoku2.txt", "grid/sudoku3.txt", "grid/sudoku4.txt", "grid/evilsudoku.txt"]
sudoku_boards = []
for file_path in sudoku_files:  
    sudoku_board = file_to_list(file_path)
    sudoku_boards.append(sudoku_board)

## PYGAME INTERFACE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()

window_size = (540, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Sudoku Solver")

font = pygame.font.Font(None, 36)

def draw_grid(board, level):
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, pygame.Rect(20, 20, 500, 500), 2)

    for i in range(1, 9):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, (20, i * 55 + 20), (520, i * 55 + 20), 3)
            pygame.draw.line(screen, BLACK, (i * 55 + 20, 20), (i * 55 + 20, 520), 3)
        else:
            pygame.draw.line(screen, BLACK, (20, i * 55 + 20), (520, i * 55 + 20), 2)
            pygame.draw.line(screen, BLACK, (i * 55 + 20, 20), (i * 55 + 20, 520), 2)

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                screen.blit(text, (j * 55 + 37, i * 55 + 30))

    pygame.draw.rect(screen, BLUE, pygame.Rect(200, 540, 140, 50))
    text = font.render("Solver", True, WHITE)
    screen.blit(text, (225, 550))

    level_text = font.render("Level " + str(level + 1), True, BLACK)
    screen.blit(level_text, (20, 540))

    pygame.display.flip()

def choose_level():
    selected_level = 0
    running = True

    while running:
        screen.fill(WHITE)

        level_text = font.render("Choose a level for Sudoku Solver:", True, BLACK)
        screen.blit(level_text, (20, 20))

        for i, board in enumerate(sudoku_boards):
            level_number = i + 1
            level_text_color = BLUE if i == selected_level else BLACK
            level_text = font.render("Level " + str(level_number), True, level_text_color)
            screen.blit(level_text, (50, 60 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_level = (selected_level - 1) % len(sudoku_boards)
                elif event.key == pygame.K_DOWN:
                    selected_level = (selected_level + 1) % len(sudoku_boards)
                elif event.key == pygame.K_RETURN:
                    return selected_level

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(len(sudoku_boards)):
                    level_rect = pygame.Rect(50, 60 + i * 50, 200, 40)
                    if level_rect.collidepoint(mouse_pos):
                        selected_level = i
                        return selected_level

        pygame.time.wait(100)


def main():
    selected_level = choose_level()
    active_level = selected_level
    sudoku_solver = BacktrackingSolver(sudoku_boards[selected_level])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= pygame.mouse.get_pos()[0] <= 340 and 540 <= pygame.mouse.get_pos()[1] <= 590:
                    sudoku_solver.solve()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    active_level = (active_level - 1) % len(sudoku_boards)
                elif event.key == pygame.K_DOWN:
                    active_level = (active_level + 1) % len(sudoku_boards)
                elif event.key == pygame.K_r:
                    selected_level = choose_level()
                    active_level = selected_level
                    sudoku_solver = BacktrackingSolver(sudoku_boards[selected_level])

        draw_grid(sudoku_boards[selected_level], active_level)

    pygame.quit()


if __name__ == "__main__":
    main()