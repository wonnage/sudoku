def same_square(row, col):
  "Return all coordinates that are in the same 3x3 box as (row,col)"
  #Here's a hint: you can start by finding the coordinate of the top left square in the 3x3 box, like this:
  same_square = []
  top_row = row - row%3
  left_col = col - col%3
  #Now you know that (top_row, left_col) is the top left square, and we want to append all nine squares
  #in the 3x3 box to same_square, then return same_square
  pass