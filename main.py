# Define the game function

# This function accepts the current game array and prints the game board
def game_board(board_array=[]):
    print('# # # # # # #\n'
          '#', board_array[0], '|', board_array[1], '|', board_array[2], '#\n'
          '# - - - - - #\n'
          '#', board_array[3], '|', board_array[4], '|', board_array[5], '#\n'
          '# - - - - - #\n'
          '#', board_array[6], '|', board_array[7], '|', board_array[8], '#\n'
          '# # # # # # #\n')


# This is the function that runs the processes of the game including
# player input and calling the game board.
def game_machine(turns=0, game_pieces=['X', 'O'], game_array=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
    # Print the game board
    game_board(game_array)

    # The while statement will keep playing the game until the turns are up
    while turns < 9:

        # The for loop alternates between both players
        for i in range(0, 2):
            print('Start turn', turns + 1, ': Player', i + 1, '!')

            # The current player will pick their next move on the board
            # with their choice going through the input validation loop.
            while True:
                selection = input('Select Location : ')
                if selection.isdigit():
                    if 0 < int(selection) < 10:

                        # The board space is replaced with the players game piece and
                        # the updated board is printed for the player.
                        game_array[int(selection) - 1] = game_pieces[i]
                        game_board(game_array)
                        break
                    else:
                        print('Please select a number on the game board')
                else:
                    print('Please select a number')

            # This next section will check to see if a player won
            # rolling through all the different winning scenarios.
            if game_array[0] == game_array[1] == game_array[2]:  # Check row 1
                print('Player', game_pieces.index(game_array[0]) + 1, 'wins!!!')
                return
            elif game_array[3] == game_array[4] == game_array[5]:  # Check row 2
                print('Player', game_pieces.index(game_array[3]) + 1, 'wins!!!')
                return
            elif game_array[6] == game_array[7] == game_array[8]:  # Check row 3
                print('Player', game_pieces.index(game_array[6]) + 1, 'wins!!!')
                return
            elif game_array[0] == game_array[3] == game_array[6]: # Check column 1
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
            else:  # If no player won, increment the turn counter and continue the game
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
