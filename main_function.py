from functions import create_board
from functions import display_board
from functions import assign_marker_to_player
from functions import space_check
from functions import mark_board
from functions import tie_game
from functions import winner_check
from functions import play_again
from functions import decide_turn
if __name__=='__main__':

    

    while True:

    	print('Welcome to the game of TIC TAC TOE')

    	board=create_board()

    	display_board(board)

    	player1_marker,player2_marker=assign_marker_to_player()

    	game_on=True

    	turn=decide_turn()


    	while game_on:

    		if turn=='Player 1':

    			display_board(board)

    			mark_board(board,player1_marker,turn)
    			if winner_check(board,player1_marker):
    				display_board(board)
    				print('Player 1 has won ')
    				game_on=False
    			elif tie_game(board):
    				print('Game has tied')
    				game_on=False
    			else:
    				turn='Player 2'

    		

    		else :

    			display_board(board)

    			mark_board(board,player2_marker,turn)
    			if winner_check(board,player2_marker):
    				display_board(board)
    				print('Player 2 has won ')
    				game_on=False
    			elif tie_game(board):
    				print('Game has tied')
    				game_on=False
    			else:
    				turn='Player 1'   


    	if not play_again():
    		print('Thanks for playing !! ')
    		break;
