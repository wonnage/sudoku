#!/usr/bin/env python3

## If you copy this file and then replace all the 'pass' statements
## with an implementation of the function, you should have a working
## Sudoku solver.

from sudoku import digits, main

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
    pass

def empty_square(board):
    "Return an empty square to try to fill."
    pass

def possible_digits(board, square):
    "Return list of digits to try putting in square s."
    pass

def assign(board, square, digit):
    "Return new board with digit d in square s."
    pass

def load_puzzle(path):
  def to_digit(chr):
    if chr=='.': return 0
    else: return int(chr)
  return [map(to_digit, line.strip().replace(' ','').replace('|','')) for line in open(path) if line.strip() and '-' not in line]

def pretty(board):
  if board is None: return 'NO SOLUTION'
  for line in board:
    return '\n'.join(''.join(map(str,line)) for line in board)

if __name__ == '__main__':
  board = load_puzzle('easy.txt')
  print ('unsolved:')
  print (pretty(board))
  print ('solved:')
  print (pretty(search(board)))
