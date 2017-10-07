# InmarChessMoves
##Inmar Coding Sample1

### Setup

- python version 2.7.1 or higher
- packages: (Installation: pip install <packageName>)
	- coverage
	- unittest
	- argparse

### Assumptions:

- Chess board : a1 - a8, b1- b8, c1- c8, d1 - d8, e1- e8, f1 - f8, g1 - g8, h1 - h8

### Steps to run program

- python chess.py -piece <pieceName> -position <position>
	- eg: python chess.py -piece queen -position h4
- Check coverage:
	- coverage run -a chess.py -piece queen -position h4
	- coverage run -a chess.py -piece rook -position h4
	- coverage run -a chess.py -piece knight -position h4
	- coverage report

### Test Coverage
![alt text](https://github.com/harshalkgurjar/InmarChessMoves/blob/master/Coverage_report.PNG)




	


