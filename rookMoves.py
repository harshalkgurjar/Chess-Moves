# function to get next possible positions of Rook
def getNextPositionsRook(position):
  column=position[0]
  row=int(position[1])
  nextPositionsRook=[]
  # All positions to left
  for i in range(1,row):
      newPosition=column+str(i)
      nextPositionsRook.append(newPosition)
  # All positions to right
  for i in range(row+1,8+1):
      newPosition=column+str(i)
      nextPositionsRook.append(newPosition)
  # All positions up
  for i in range(ord('a'),ord(column)):
      newPosition=chr(i)+str(row)
      nextPositionsRook.append(newPosition)
  # All positions down
  for i in range(ord(column)+1,ord('h')+1):
      newPosition=chr(i)+str(row)
      nextPositionsRook.append(newPosition)
  return nextPositionsRook
