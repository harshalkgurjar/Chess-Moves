# function to get next possible positions of knight
def getNextPositionsKnight(position):
  # Knight two and half moves
  column=position[0]
  row=int(position[1])
  # posible directions for knight to move
  deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
  nextPositionsKnight = []
  for (x, y) in deltas:
	#print('in for knight')
	colValue = ord(column)+x
	rowValue = row+y
	if ord('a') <= colValue <= ord('h') and 1 <= rowValue <= 8:
		nextPositionsKnight.append(chr(colValue)+str(rowValue))
  return nextPositionsKnight
