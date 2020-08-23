def create_board():

	board=['#','','','','','','','','','']
	return board

def display_board(board):
	
	
	print(board[7]+' | '+board[8]+' | '+board[9])
	print('------')
	print(board[4]+' | '+board[5]+' | '+board[6])
	print('------')
	print(board[1]+' | '+board[2]+' | '+board[3])
	

def assign_marker_to_player():
	player1_marker=''
	while player1_marker not in ['X','O']:
		player1_marker=input('Player1, please choose a valid marker[X/O]').upper()

	if player1_marker=='X':
		player2_marker='O'
	
	else:
		player2_marker='X'
		

	return(player1_marker,player2_marker)


def space_check(board,position):
	if board[position]=='':
		return True
	else:
		return False

def mark_board(board,player_marker,turn):

	pos=0
	while pos  not in range(1,10) or not space_check(board,pos):
		pos=int(input(turn+', Plese enter a valid position '))
	board[pos]=player_marker




		


def tie_game(board):

	if '' not in board:
		return True
	
	return False

def winner_check(board,mark):
	 return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def play_again():

	ans=''

	while ans not in['Y','N']:

		ans=input('Do you want to play again? Please enter [Y/N] ').upper()

	if ans=='Y':
		return True

	else:
		return False

def decide_turn():

	import random

	flip=random.choice([2,1])

	if flip==1:
		print('Player 1 will play first')
		return "Player 1"
	else:
		print('player 2 will play first ')
		return "Player2"


