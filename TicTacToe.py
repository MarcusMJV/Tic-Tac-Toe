import random

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
run = True


# This function creates the list from the pre-defined list
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# This function puts all the functions together and runs the game
def play():
    display_board()
    while run:
        turn()
    play_again()


# This function allows the user and computer take a turn
def turn():
    global run
    player_turn = True

    # Players turn
    if player_turn:
        while True:
            try:
                command = int(input('Please choose a position to enter the X between 1 to 9: '))
                if board[command - 1] == '-':
                    board[command - 1] = 'X'
                    display_board()
                    check_win_or_tie()
                    if not run:
                        break
                    else:
                        player_turn = False
                        break
                elif board[command - 1] == 'X' or board[command - 1] == 'O':
                    print('Sorry space is not available please choose again')
            except ValueError:
                print('Please enter a number')
            except IndexError:
                print('Please enter the correct number')

    # Computers turn
    if not player_turn:
        while True:
            computer_command = random.randint(1, 9)
            if board[computer_command - 1] == '-':
                board[computer_command - 1] = 'O'
                print(f'The computer placed a O at position {computer_command}')
                display_board()
                check_win_or_tie()
                if not run:
                    break
                else:
                    player_turn = True
                    break
            elif board[computer_command - 1] == 'X' or board[computer_command - 1] == 'O':
                continue


# This function checks the board and to see if someone won or if there is a tie
def check_win_or_tie():
    column = 0
    row = 0
    diagonal = 0
    tie = 9
    global run

    # Check rows
    for i in range(3):
        if (board[0 + column] == 'X') and (board[1 + column] == 'X') and (board[2 + column] == 'X'):
            print('Congratulations you win!!!')
            run = False
        if (board[0 + column] == 'O') and (board[1 + column] == 'O') and (board[2 + column] == 'O'):
            print('Sorry you lose the computer wins!!!')
            run = False
        column += 3

    # Check columns
    for i in range(3):
        if (board[0 + row] == 'X') and (board[3 + row] == 'X') and (board[6 + row] == 'X'):
            print('Congratulations you win!!!')
            run = False
        if (board[0 + row] == 'O') and (board[3 + row] == 'O') and (board[6 + row] == 'O'):
            print('Sorry you lose the computer wins!!!')
            run = False
        row += 1

    # Check diagonal
    for i in range(2):
        if (board[2 - diagonal] == 'X') and (board[4] == 'X') and (board[6 + diagonal] == 'X'):
            print('Congratulations you win!!!')
            run = False
        if (board[2 - diagonal] == 'O') and (board[4] == 'O') and (board[6 + diagonal] == 'O'):
            print('Sorry you lose the computer wins!!!')
            run = False
        diagonal += 2

    for i in board:
        if i != '-':
            tie -= 1
    if tie == 0 and run:
        print('Game is a tie!!! Thank you for playing')
        run = False


# This function will ask the user if they want to play again and resets the board
def play_again():
    global board
    global run
    while True:
        x = input('Would you like to play again? (y/n) ')
        if x == 'y':
            run = True
            board = ['-', '-', '-',
                     '-', '-', '-',
                     '-', '-', '-']
            play()
            break

        elif x == 'n':
            break

        else:
            print('Sorry wrong input')


play()
