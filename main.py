# Define the game function

def game_board(array=[]):
    print('# # # # # # #\n'
          '#', array[0], '|', array[1], '|', array[2], '#\n'
          '# - - - - - #\n'
          '#', array[3], '|', array[4], '|', array[5], '#\n'
          '# - - - - - #\n'
          '#', array[6], '|', array[7], '|', array[8], '#\n'
          '# # # # # # #\n')


def game_machine(turns=0, game_pieces=['X', 'O'], game_array=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
    # Print the game board
    game_board(game_array)

    # The while statement will keep playing the game until the turns are up
    while turns < 9:
        # The for loop alternates between both players
        for i in range(0, 2):
            print('Start turn', turns + 1, ': Player', i + 1, '!')

            # The current player will pick their next move on the board by choosing a number on the board
            selection = int(input('Select Location : '))  # TODO add input validation
            game_array[selection - 1] = game_pieces[i]  # The board space is replaced with the players game piece
            game_board(game_array)  # Print the game board with the updated changes

            # This next section will check to see if a player won

            if game_array[0] == game_array[1] == game_array[2]:  # Check row 1
                print('Player', game_pieces.index(game_array[0]) + 1, 'wins!!!')
                return
            elif game_array[3] == game_array[4] == game_array[5]:  # Check row 2
                print('Player', game_pieces.index(game_array[3]) + 1, 'wins!!!')
                return
            elif game_array[6] == game_array[7] == game_array[8]:  # Check row 3
                print('Player', game_pieces.index(game_array[6]) + 1, 'wins!!!')
                return
            elif game_array[0] == game_array[3] == game_array[6]:  # Check column 1
                print('Player', game_pieces.index(game_array[0]) + 1, 'wins!!!')
                return
            elif game_array[1] == game_array[4] == game_array[7]:  # Check column 2
                print('Player', game_pieces.index(game_array[1]) + 1, 'wins!!!')
                return
            elif game_array[2] == game_array[5] == game_array[8]:  # Check column 3
                print('Player', game_pieces.index(game_array[2]) + 1, 'wins!!!')
                return
            elif game_array[0] == game_array[4] == game_array[8]:  # Check diagonal top left to bottom right
                print('Player', game_pieces.index(game_array[0]) + 1, 'wins!!!')
                return
            elif game_array[2] == game_array[4] == game_array[6]:  # Check diagonal top right to bottom left
                print('Player', game_pieces.index(game_array[2]) + 1, 'wins!!!')
                return
            else:  # If no player one, increment the turn counter and continue the game
                turns += 1


# Begin program

# Print welcome statement
print('''
Welcome to Tik Tac Toe!
Player 1 will be "X"
Player 2 will be "O"
Pick a location on the board to place your pieces!
''')

# Start the game by calling the function
game_machine()

# Print goodbye statement
print('Thank you for playing!')

# End program
