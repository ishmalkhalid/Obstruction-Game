
#import headers
import random

#declare constants
NUM_PLAYERS = 2
board = []
PLAYERS = [' X ',' O ']

#enter row and column dimensions
NUM_ROWS = int(input("Enter the row dimensions."))
NUM_COLS = int(input("Enter the column dimensions."))

while (NUM_ROWS > 26 or NUM_COLS > 26):
	NUM_ROWS = int(input("Invalid dimensions. Pleasee re-enter the row dimensions."))
	NUM_COLS = int(input("Invalid dimensions. Pleasee re-enter the column dimensions."))

#print column numbers
print('  ')
for cols in range(NUM_COLS):
	print('   ' + str(chr(cols+65)), end='')

#print first line underneath column numbers
print('\n +'+'---+'*NUM_COLS)

#create board
for row in range (NUM_ROWS):
	row_list=[]
	for col in range (NUM_COLS):
		row_list.append(' . ')
	board.append(row_list)

#print rest of the board
for row in range(NUM_ROWS):
	print(str(row) + '|', end='')
	for col in range(NUM_COLS):
		print(board[row][col] + '|', end='')
	print('\n +' + '---+'*NUM_COLS)
 
#random player choosen
# PLAYER1 = 'X'
# PLAYER2 = 'O'

turn= PLAYERS[random.randint(0, 1)]
if turn ==0:
	first_turn = PLAYERS[0]
	second_turn=PLAYERS[1]
else:
	second_turn=PLAYERS[0]
	first_turn = PLAYERS[1]

win = False
take_turn=0

while win == False:
	win=True

	if take_turn ==0:

		#check whether the input is valid or not
		checker_position = input("Enter the coordinates to place your checker.")
		
		#check whether the input is valid or not
		while not len(checker_position)<3 or not checker_position[0].isalpha() or not checker_position[1:].isdigit() or not 65<=int(ord(checker_position[0].capitalize()))<(NUM_COLS+65-1) or not 0<=int(checker_position[1:])<=(NUM_ROWS):
			print("ERROR!!!! Enter valid input")
			checker_position = input("Enter the coordinates to place your checker.")
		lett2numcoord = ord((checker_position[0]).capitalize())-65
		rowcoord = int(checker_position[1])
		while board[rowcoord][lett2numcoord]!=' . ':
			print("ERROR!!!! Enter valid input")
			checker_position = input("Enter the coordinates to place your checker.")
			while not len(checker_position)<3 or not checker_position[0].isalpha() or not checker_position[1:].isdigit() or not 65<=int(ord(checker_position[0].capitalize()))<(NUM_COLS+65-1) or not 0<=int(checker_position[1:])<=(NUM_ROWS):
				print("ERROR!!!! Enter valid input")
				checker_position = input("Enter the coordinates to place your checker.")
			lett2numcoord = ord((checker_position[0]).capitalize())-65
			rowcoord = int(checker_position[1])


		board[rowcoord][lett2numcoord]=first_turn
#BLOCK CELLS		
		if rowcoord>0  and board[rowcoord-1][lett2numcoord]==" . ":
			board[rowcoord-1][lett2numcoord]=" # "

		if rowcoord>0  and lett2numcoord>0 and board[rowcoord-1][lett2numcoord-1]==" . ":			
			board[rowcoord-1][lett2numcoord-1]=" # "
		
		if rowcoord>0 and lett2numcoord<(NUM_COLS) and board[rowcoord-1][lett2numcoord+1]==" . ":			
			board[rowcoord-1][lett2numcoord+1]=" # "

		if rowcoord<NUM_ROWS and board[rowcoord+1][lett2numcoord]==" . ":			
			board[rowcoord+1][lett2numcoord]=" # "

		if rowcoord<NUM_ROWS and lett2numcoord>0 and board[rowcoord+1][lett2numcoord-1]==" . ":			
			board[rowcoord+1][lett2numcoord-1]=" # "

		if rowcoord<NUM_ROWS and lett2numcoord<NUM_COLS and board[rowcoord+1][lett2numcoord+1]==" . ":			
			board[rowcoord+1][lett2numcoord+1]=" # "
	
		if lett2numcoord<NUM_COLS and board[rowcoord][lett2numcoord+1]==" . ":			
			board[rowcoord][lett2numcoord+1]=" # "

		if lett2numcoord>0 and board[rowcoord][lett2numcoord-1]==" . ":			
			board[rowcoord][lett2numcoord-1]=" # "
		
		for cols in range(NUM_COLS):
			print('   ' + str(chr(cols+65)), end='')
		print('\n +'+'---+'*NUM_COLS)
		
		for row in range(NUM_ROWS):
			print(str(row) + '|', end='')
			for col in range(NUM_COLS):
				print(board[row][col] + '|', end='')
			print('\n +' + '---+'*NUM_COLS)

	#winning condition and printing statement for winner:
	for row in range(NUM_ROWS):
		for col in range(NUM_COLS):
			if board[row][col] == " . ":
				win = False
	take_turn= take_turn+1
	
	if win== True:
		print("GAME OVER!", "\n", "Player", first_turn, "won!" )


	if take_turn==1:
		#prompt user for location of checker
		
		checker_position = input("Enter the coordinates to place your checker.")
		
		#check whether the input is valid or not
		while not len(checker_position)<3 or not checker_position[0].isalpha() or not checker_position[1:].isdigit() or not 65<=int(ord(checker_position[0].capitalize()))<(NUM_COLS+65-1) or not 0<=int(checker_position[1:])<=(NUM_ROWS):
			print("ERROR!!!! Enter valid input")
			checker_position = input("Enter the coordinates to place your checker.")
		lett2numcoord = ord((checker_position[0]).capitalize())-65
		rowcoord = int(checker_position[1])

		while board[rowcoord][lett2numcoord]!=' . ':
			print("ERROR!!!! Enter valid input")
			checker_position = input("Enter the coordinates to place your checker.")
			while not len(checker_position)<3 or not checker_position[0].isalpha() or not checker_position[1:].isdigit() or not 65<=int(ord(checker_position[0].capitalize()))<(NUM_COLS+65-1) or not 0<=int(checker_position[1:])<=(NUM_ROWS):
				print("ERROR!!!! Enter valid input")
				checker_position = input("Enter the coordinates to place your checker.")
			lett2numcoord = ord((checker_position[0]).capitalize())-65
			rowcoord = int(checker_position[1])

	
	
		board[rowcoord][lett2numcoord]=second_turn
		
		if rowcoord>0  and board[rowcoord-1][lett2numcoord]==" . ":
			board[rowcoord-1][lett2numcoord]=" # "

		if rowcoord>0  and lett2numcoord>0 and board[rowcoord-1][lett2numcoord-1]==" . ":			
			board[rowcoord-1][lett2numcoord-1]=" # "
		
		if rowcoord>0 and lett2numcoord<(NUM_COLS) and board[rowcoord-1][lett2numcoord+1]==" . ":			
			board[rowcoord-1][lett2numcoord+1]=" # "

		if rowcoord<(NUM_ROWS-1) and board[rowcoord+1][lett2numcoord]==" . ":			
			board[rowcoord+1][lett2numcoord]=" # "

		if rowcoord<(NUM_ROWS-1) and lett2numcoord>0 and board[rowcoord+1][lett2numcoord-1]==" . ":			
			board[rowcoord+1][lett2numcoord-1]=" # "

		if rowcoord<(NUM_ROWS-1) and lett2numcoord<NUM_COLS and board[rowcoord+1][lett2numcoord+1]==" . ":			
			board[rowcoord+1][lett2numcoord+1]=" # "
	
		if lett2numcoord<NUM_COLS and board[rowcoord][lett2numcoord+1]==" . ":			
			board[rowcoord][lett2numcoord+1]=" # "

		if lett2numcoord>0 and board[rowcoord][lett2numcoord-1]==" . ":			
			board[rowcoord][lett2numcoord-1]=" # "
		
		for cols in range(NUM_COLS):
			print('   ' + str(chr(cols+65)), end='')
		print('\n +'+'---+'*NUM_COLS)
		
		for row in range(NUM_ROWS):
			print(str(row) + '|', end='')
			for col in range(NUM_COLS):
				print(board[row][col] + '|', end='')
			print('\n +' + '---+'*NUM_COLS)


		for row in range(NUM_ROWS):
			for col in range(NUM_COLS):
				if board[row][col] == " . ":
					win = False
		take_turn= 0
		if win==True:
			print("GAME OVER!", "\n", "Player", first_turn, "won!" )






