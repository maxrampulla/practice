puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def sudoku(puzzle):
  while check(puzzle):
    traverse(puzzle)
    lessen(puzzle)
    eliminate(puzzle)
  return puzzle


def lessen(puzzle):
  for row in puzzle:
    rowCounter = 0 
    for i in row:
      if isinstance(i, list):
          row[rowCounter] = removal(i)
      rowCounter += 1


def removal(list):
  total = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  for i in list:
    for n in total:
      if n == i:
        total.remove(n)
  
  return total


def eliminate(puzzle):
  for row in puzzle:
    rowCounter = 0 
    for i in row:
      if isinstance(i, list):
        if len(i) == 1:
          row[rowCounter] = i[0]
      rowCounter += 1


#checks if puzzle has been solved 
def check(puzzle):
  for row in puzzle:
    for i in row:
      if isinstance(i, list):
        return True
      elif i == 0:
        return True
  return False


# creates a list of all unusable options for this part 
def traverse(puzzle):
  rowCount = 0
  for row in puzzle:
    Colcounter = 0
    for i in row:
      if i == 0 or isinstance(i, list):
        row[Colcounter] = rowFind(row) + columnFind(puzzle, Colcounter) + quadFind(puzzle, whichQuad(Colcounter, rowCount))
      Colcounter += 1
    rowCount += 1


# retuns list of numbers in column 
def columnFind(puzzle, columnInt):
  valueList = []
  for i in puzzle:
    if i[columnInt] != 0 and isinstance(i[columnInt], int):
      valueList.append(i[columnInt])
  return valueList
  

#returns list of numbers in row 
def rowFind (row):
  valueList = []
  for i in row:
    if isinstance(i, int) and i > 0:
      valueList.append(i)
  
  return valueList


#determins the quadrant
def whichQuad(column, row):
  if column >= 0 and column <= 2 :
    if row >= 0 and row <= 2: 
      return 0
    elif row >= 3 and row <= 5: 
      return 3
    elif row >= 6 and row <= 8:
      return 6
  elif column >= 3 and column <= 5:
    if row >= 0 and row <= 2: 
      return 1
    elif row >= 3 and row <= 5: 
      return 4
    elif row >= 6 and row <= 8:
      return 7
  elif column >= 6 and column <= 8:
    if row >= 0 and row <= 2: 
      return 2
    elif row >= 3 and row <= 5: 
      return 5
    elif row >= 6 and row <= 8:
      return 8

#returns list of numbers in quadrant
def quadFind (puzzle, quad):
  quads = [[],[],[],[],[],[],[],[],[]]

  rowCount = 0
  for row in puzzle:
    columnCount = 0
    for i in row:
      if isinstance(i, int) and i > 0:
        if columnCount >= 0 and columnCount <= 2:
          if rowCount >= 0 and rowCount <= 2: 
            quads[0].append(i)
          elif rowCount >= 3 and rowCount <= 5: 
            quads[3].append(i)
          elif rowCount >= 6 and rowCount <= 8:
            quads[6].append(i)
        elif columnCount >= 3 and columnCount <= 5:
          if rowCount >= 0 and rowCount <= 2: 
            quads[1].append(i)
          elif rowCount >= 3 and rowCount <= 5: 
            quads[4].append(i)
          elif rowCount >= 6 and rowCount <= 8:
            quads[7].append(i)
        elif columnCount >= 6 and columnCount <= 8:
          if rowCount >= 0 and rowCount <= 2: 
            quads[2].append(i)
          elif rowCount >= 3 and rowCount <= 5: 
            quads[5].append(i)
          elif rowCount >= 6 and rowCount <= 8:
            quads[8].append(i)
      columnCount += 1
    rowCount += 1
  return (quads[quad])


            
if __name__ == "__main__":
  sudoku(puzzle)
  