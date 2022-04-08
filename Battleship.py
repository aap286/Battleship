from random import randint
from colorama import init
from termcolor import colored

init()

# list of letters:
low_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

up_case_letters = []
for letter in low_case_letters:
    up_case_letters.append(letter.upper())

# creating dictiornary for correspinding letters:
dict = {}

for index in range(len(up_case_letters)):
    dict[up_case_letters[index]] = index + 1


# creating the board:

board = []  # board list


# inital board_maker
def board_maker(board, n):  # where n is the number of columns

    for i in range(n+1):
        board.append([colored('O', 'cyan')] * (n+1))

# re-defining column names


def board_label(board, n):

    for i in range(n):
        board[0][i+1] = colored(str(i + 1), 'yellow'
                                )
        board[i+1][0] = colored(up_case_letters[i], 'yellow')

    board[0][0] = " "


# prints board with no commas:
def print_board(board, n):

    for row in board:
        print(" ".join(row))


# planting the ship:

# guessing the row:
def guess_row(board, n):
    row = up_case_letters[randint(1, n - 1)]
    return row


def guess_col(board, n):
    col = randint(1, n)
    return col


def user_guess(n):  # user_guess, n number of rows

    row = user_row_guess(n, "")
    col = user_col_guess(n, "")

    return row, col


def user_row_guess(n, x):   # user_row guess
    row = input("Guess Row {gin}: ".format(gin=x).center(30)).upper()

    if row.upper() in up_case_letters:
        if dict[row] <= n and len(row) == 1:
            return row
        else:
            print("Oops, that's not even in the ocean. \n".center(50))
            return user_row_guess(n, "again")

    else:
        print("Oops, that's not even in the ocean. \n".center(50))
        return user_row_guess(n, "again")


def user_col_guess(n, x):   # user_column guess
    col = input("Guess Col {gin}: ".format(gin=x).center(30))

    if col.upper() not in up_case_letters and col.isdigit():

        col = int(col)
        if col in range(1, n+1):
            return col
        else:
            print("Incorrect water space! \n".center(45))
            return user_col_guess(n, "encore")
    else:
        print("Incorrect water space! \n".center(45))
        return user_col_guess(n, "encore")

# looping the game


def the_game_loop(board, n):

    # ship location
    ship_row = guess_row(board, n)
    ship_col = guess_col(board, n)

    # ship coordinates
    #print("Ship coordinate: {}{}".format(ship_row, ship_col))
    print("\n")

    # board formation
    board_maker(board, n)
    board_label(board, n)

    print("Aye, aye, Captain here is your grid to assault attacks \n")

    print_board(board, n)
    print("\n")

    for turn in range(4):

        # printing the board
        if turn != 4:
            print("Turn {turn}:".format(turn=turn + 1).center(10))

        else:
            print("Final turn:".center(10))

        # user's guess
        u_row, u_col = user_guess(n)

        print("\n")

        if u_row == ship_row and int(u_col) == ship_col:

            board[dict[u_row]][u_col] = colored("¤", 'grey', 'on_green')
            print_board(board, n)
            print("\n")
            print("Congratulations! You sank my battleship! \n")
            exit()

        else:
            # print(dict[u_row])
            # print(type(u_col))
            board[dict[u_row]][u_col] = colored('𝕏', 'white', 'on_red')
            print_board(board, n)
            print("\n")
            print("You missed my battleship! \n")

        if turn == 3:

            print("Game Over. Good luck next time Captain")
            print("\n")


the_game_loop(board, 4)
