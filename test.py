import unittest
import io
import sys
import chess as ch
import queenMoves as qm
import rookMoves as rm
import knightMoves as km
class MainTest(unittest.TestCase):
	# test to check valid input for queen from main method
	def test_main_valid_input_queen(self):
		sys.argv=["py","-piece", "queen", "-position", "h4"]
		expected_output=['h1', 'h2', 'h3', 'h5', 'h6', 'h7', 'h8', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'g3', 'f2', 'e1', 'g5', 'f6', 'e7', 'd8']
		result=ch.main()
		self.assertEqual(result, expected_output)
	# test to check valid input for knight from main method
	def test_main_valid_input_knight(self):
		sys.argv=["py","-piece", "knight", "-position", "h4"]
		expected_output=['f3', 'f5', 'g2', 'g6']
		result=ch.main()
		self.assertEqual(result, expected_output)
	# test to check valid input for rook from main method
	def test_main_valid_input_rook(self):
		sys.argv=["py","-piece", "rook", "-position", "h4"]
		expected_output=['h1', 'h2', 'h3', 'h5', 'h6', 'h7', 'h8', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4']
		result=ch.main()
		self.assertEqual(result, expected_output)
	# input for invalid position
	def test_main_invalid_position(self):
		sys.argv=["py","-piece", "queen", "-position", "n5"]
		expected_value=-1
		result=ch.main()
		self.assertEqual(result,expected_value)
	# input for invalid piece	
	def test_main_invalid_piece(self):
		sys.argv=["py","-piece", "king", "-position", "h4"]
		expected_value=-1
		result=ch.main()
		self.assertEqual(result,expected_value)
	# test to check valid input for queen from queen method
	def test_queen(self):
		expected_output=['h1', 'h2', 'h3', 'h5', 'h6', 'h7', 'h8', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'g3', 'f2', 'e1', 'g5', 'f6', 'e7', 'd8']
		result=qm.getNextPositionsQueen("h4")
		self.assertEqual(result, expected_output)
	# test to check valid input for rook from rook method
	def test_rook(self):
		expected_output=['h1', 'h2', 'h3', 'h5', 'h6', 'h7', 'h8', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4']
		result=rm.getNextPositionsRook("h4")
		self.assertEqual(result, expected_output)
	# test to check valid input for knight from knight method
	def test_knight(self):
		expected_output=['f3', 'f5', 'g2', 'g6']
		result=km.getNextPositionsKnight('h4')
		self.assertEqual(result, expected_output)