# function to get next possible positions of Bishop
def getNextPositionsBishop(position):
  column=position[0]
  row=int(position[1])
  nextPositionsBishop=[]
  ##Bishop can travel only diagonally
  ## All possible top left
  for i, j in zip(range(ord(column)-1,ord('a')-1,-1), range(row-1,1-1,-1)):
	newPosition=chr(i)+str(j)
	nextPositionsBishop.append(newPosition)
	
  ## All possible bottom right
  for i, j in zip(range(ord(column)+1, ord('h')+1), range(row+1, 8+1)):
	newPosition=chr(i)+str(j)
	nextPositionsBishop.append(newPosition)

  ## All possible top right
  for i, j in zip(range(ord(column)+1,ord('h')+1), range(row-1,1-1,-1)):
	newPosition=chr(i)+str(j)
	nextPositionsBishop.append(newPosition)
	
  ## All possible bottom left
  for i, j in zip(range(ord(column)-1,ord('a')-1,-1), range(row+1,8+1)):
	newPosition=chr(i)+str(j)
	nextPositionsBishop.append(newPosition)
	
  return nextPositionsBishop  
  
