import random
import os
import keyboard

def initialize_game():
    return [[0] * 4 for _ in range(4)]

def print_board(board):
    os.system("clear" if os.name == "posix" else "cls")
    print("2048 Game:")
    for row in board:
        print(" ".join(str(cell) if cell != 0 else "." for cell in row))
    print()

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

def move(board, direction):
    for _ in range(4):
        row = board[_]
        if direction == "left":
            board[_] = merge_tiles(row)
        elif direction == "right":
            board[_] = merge_tiles(row[::-1])[::-1]
        elif direction == "up":
            col = [board[i][_] for i in range(4)]
            merged_col = merge_tiles(col)
            for i in range(4):
                board[i][_] = merged_col[i]
        elif direction == "down":
            col = [board[i][_] for i in range(3, -1, -1)]
            merged_col = merge_tiles(col)
            for i in range(4):
                board[i][_] = merged_col[3 - i]

def merge_tiles(line):
    merged_line = [0] * 4
    merged_line_index = 0

    for value in line:
        if value != 0:
            if merged_line[merged_line_index] == 0:
                merged_line[merged_line_index] = value
            elif merged_line[merged_line_index] == value:
                merged_line[merged_line_index] *= 2
                merged_line_index += 1
            else:
                merged_line_index += 1
                merged_line[merged_line_index] = value

    return merged_line

def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
    return True

def play_game():
    board = initialize_game()
    add_new_tile(board)
    add_new_tile(board)
    print_board(board)

    while not is_game_over(board):
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            move(board, "down")
        elif event.event_type == keyboard.KEY_UP:
            move(board, "up")
        elif event.event_type == keyboard.KEY_LEFT:
            move(board, "left")
        elif event.event_type == keyboard.KEY_RIGHT:
            move(board, "right")

        add_new_tile(board)
        print_board(board)

    print("Game over!")

if __name__ == "__main__":
    play_game()




