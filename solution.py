#!/usr/bin/env python2.7

## If you copy this file and then replace all the 'pass' statements
## with an implementation of the function, you should have a working
## Sudoku solver.

import copy

#
# Recursive depth first search
#
def search(board):
    if board is None or solved(board): return board

    square = empty_square(board)
    for digit in possible_digits(board, square):
        solution = search(assign(board, square, digit))
        if solution: return solution

    return None

def solved(board):
    "Returns true if the given board is already solved."
    for line in board:
      if 0 in line: return False
    return True

def empty_square(board):
    "Return an empty square to try to fill."
    for y, line in enumerate(board):
      for x, cell in enumerate(line):
        if cell==0: return (x,y)

def square_of(x,y):
  "Return a list of all coordinates that are in the same 3x3 square as (x,y)"
  # upper left square of the 3x3 square
  x0 = x - x%3
  y0 = y - y%3
  # final answer
  return [(x0 + dx, y0 + dy) for dx in range(3) for dy in range(3)]

def possible_digits(board, square):
    "Return list of digits to try putting in square s."
    forbidden = set()
    x, y = square
    for other_x in range(9):
      forbidden.add(board[y][other_x])
    for other_y in range(9):
      forbidden.add(board[other_y][x])
    for other_x, other_y in square_of(x,y):
      forbidden.add(board[other_y][other_x])
    return set(range(1,10)) - forbidden

def assign(board, square, digit):
    "Return new board with digit d in square s."
    new_board = copy.deepcopy(board)
    x, y = square
    assert board[y][x] == 0
    new_board[y][x] = digit
    assert board[y][x] == 0
    return new_board

def load_puzzle(path):
  def to_digit(chr):
    if chr=='.': return 0
    else: return int(chr)
  return [[to_digit(chr) for chr in line.strip().replace(' ','').replace('|','')] for line in open(path) if line.strip() and '-' not in line]

def show(board):
  if board is None: return 'NO SOLUTION'
  for y, line in enumerate(board):
    if y%3 == 0 and y != 0: print('------+-------+------')
    print('%s %s %s | %s %s %s | %s %s %s' % tuple(line))

if __name__ == '__main__':
  board = load_puzzle('easy.txt')

  print('unsolved:')
  show(board)
  print('solved:')
  show(search(board))
