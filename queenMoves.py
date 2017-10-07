import rookMoves as rm
import bishopMoves as bm
# function to get next possible positions of Queen
def getNextPositionsQueen(position):
  nextPositionsQueen=[]
  ##Queen can travel all the positions of Rook and Bishop
  nextPositionsQueen = rm.getNextPositionsRook(position)
  nextPositionsQueen += bm.getNextPositionsBishop(position)
  return nextPositionsQueen
