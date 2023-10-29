from numpy import random

def build_board(size):
    board = random.choice(['Empty', 'Red', 'Black'], (size, size))
    return board

def get_count(board, cell_type):
    total = (board == cell_type)
    print(f'The number of {cell_type} cells is:')
    return total.sum()

if __name__ == "__main__":
    print("Please do not run this file directly. It should be imported from a separate main.py file.")
