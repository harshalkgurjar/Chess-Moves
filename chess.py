import sys
import argparse
import bishopMoves as bm
import queenMoves as qm
import rookMoves as rm
import knightMoves as km
#list of valid chess pieces
KNIGHT='knight'
QUEEN='queen'
ROOK='rook'
validPiecesList=[KNIGHT, QUEEN, ROOK]

#function to check if given piece is among validPiecesList=[KNIGHT, QUEEN, ROOK]
def isValidPiece(piece):
  if(piece in validPiecesList):
    #print ('Valid piece')
    return True
  else:
    #print ('Invalid piece')
    return False

#function to check if given position is a valid chess position
#valid postion ranges from a1 -a8, b1- b8,..., h1- h8
def isValidPosition(position):
  if len(position) > 2:
      print 'Invalid Position. Please Enter position between a1-a8, b1-b8,..., h1-h8 '
      return False
  position1=position[0]
  position2=position[1]
  if (position[0] >='a' and position[0] <= 'h') and (position[1] >= '1' and position[1] <= '8'):
      #print('Valid Position')
      return True
  print 'Invalid Position2. Please Enter position between a1-a8, b1-b8,..., h1-h8'
  return False

# function to check if given input is valid
def isValidInput(piece,position):
  return (isValidPiece(piece) and isValidPosition(position))

#function to get next possible move for a given piece
def getNextPositions(piece, position):
  nextPossiblePositions=[]  
  if(piece=='knight'):
      return km.getNextPositionsKnight(position);
  elif(piece=='queen'):
      return qm.getNextPositionsQueen(position);
  elif(piece=='rook'):
      return rm.getNextPositionsRook(position);

# #Main function to take input and display output
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-piece", help="Chess Piece")
	parser.add_argument("-position", help="Initial position for chess piece")
	args = parser.parse_args()
	piece=args.piece.lower()
	position=args.position.lower()
	result = None
	nextPositions=[]
	if(isValidInput(piece,position)):
		nextPositions=getNextPositions(piece, position)
	else:
		return -1
	print (nextPositions)
	return nextPositions
	
if __name__== "__main__":
	main()
