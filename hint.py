def square_of(x,y):
  "Return a list of all coordinates that are in the same 3x3 square as (x,y)"
  # upper left square of the 3x3 square
  x0 = x - x%3
  y0 = y - y%3
  # final answer
  return [(x0 + dx, y0 + dy) for dx in range(3) for dy in range(3)]

import copy
def assign(board, square, digit):
    "Return new board with digit d in square s."
    new_board = copy.deepcopy(board)
    x, y = square
    new_board[y][x] = digit
    return new_board
