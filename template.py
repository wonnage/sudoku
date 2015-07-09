#!/usr/bin/env python2.7

## If you copy this file and then replace all the 'pass' statements
## with an implementation of the function, you should have a working
## Sudoku solver.

#
# Recursive depth first search
#

#Topics to cover in introduction: 2D arrays, DFS, recursion, creating an empty list, appending to a list, creating a set, discarding from a set (remove causes KeyError, discard doesn't)

import copy

def solve(board):
    if board is None or solved(board): return board

    (row, col) = empty_square(board)
    for digit in possible_digits(board, row, col):
        assigned_board = assign(board, row, col, digit)
        solution = solve(assigned_board)
        if solution is not None:
            return solution

    # If we came this far, "return solution" above was never called; in other
    # words, no solution was found. Return None to indicate that.
    return None

def solved(board):
    "Return True if all the squares are filled in. Return False if there are any empty squares."
    raise NotImplementedError

def empty_square(board):
    "Find an empty square. (Empty squares have a 0 in them.) Return the (row, col) of the empty square. If there are no empty squares, return None."
    raise NotImplementedError
    
def same_row(row, col):
    "Return a list of all the coordinates that are in the same row as (row, col)."
    raise NotImplementedError

def same_col(row, col):
    "Return a list of all the coordinates that are in the same column as (row, col)."
    raise NotImplementedError
    
def same_square(row, col):
    "Return all coordinates that are in the same 3x3 box as (row,col)"
    raise NotImplementedError
  
def possible_digits(board, row, col):
    "Return list of all the digits that are allowed to go in the square (row, col)."
    raise NotImplementedError

def assign(board, row, col, digit):
    "Make a deep copy of the board, using new_board = copy.deepcopy(board) Then assign digit to the square (row, col) and return new_board"
    new_board = copy.deepcopy(board)
    new_board[row][col] = digit
    return new_board

### Loading boards from a file, showign them on the screen -- you don't need to change this

def load_puzzle(path):
  def to_digit(chr):
    if chr=='.': return 0
    else: return int(chr)
  return [map(to_digit, line.strip().replace(' ','').replace('|','')) for line in open(path) if line.strip() and '-' not in line]

def show(board):
  if board is None: return 'NO SOLUTION'
  for y, line in enumerate(board):
    if y%3 == 0 and y != 0: print('------+-------+------')
    print('%s %s %s | %s %s %s | %s %s %s' % tuple(line))

### Starting point of the program. Load a board (you can change which!), call solve() to solve it

if __name__ == '__main__':
  board = load_puzzle('easy.txt')
  print('Unsolved board:')
  show(board)
  print('Your solution:')
  show(solve(board))
