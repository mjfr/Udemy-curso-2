# TODO 1 - Build a text-based version of the Tic Tac Toe game.

ASCII_TITLE = " _______  _______ _________ _______\n" \
              "(  ____ \\(  ____ )\\__   __/(  ____ \\\n" \
              "| (    \\/| (    )|   ) (   | (    \\/\n" \
              "| (__    | (____)|   | |   | |\n" \
              "|  __)   |  _____)   | |   | |\n" \
              "| (      | (         | |   | |\n" \
              "| (____/\\| )      ___) (___| (____/\\\n" \
              "(_______/|/       \\_______/(_______/\n" \
              "__________________ _______   _________ _______  _______   _________ _______  _______  _\n" \
              "\\__   __/\\__   __/(  ____ \\  \\__   __/(  ___  )(  ____ \\  \\__   __/(  ___  )(  ____ \\( )\n" \
              "   ) (      ) (   | (    \\/     ) (   | (   ) || (    \\/     ) (   | (   ) || (    \\/| |\n" \
              "   | |      | |   | |           | |   | (___) || |           | |   | |   | || (__    | |\n" \
              "   | |      | |   | |           | |   |  ___  || |           | |   | |   | ||  __)   | |\n" \
              "   | |      | |   | |           | |   | (   ) || |           | |   | |   | || (      (_)\n" \
              "   | |   ___) (___| (____/\\     | |   | )   ( || (____/\\     | |   | (___) || (____/\\ _\n" \
              "   )_(   \\_______/(_______/     )_(   |/     \\|(_______/     )_(   (_______)(_______/(_)\n\n\n"
error_color = "\033[91m"
normal_color = "\033[0m"
win_color = "\033[92m"
x_color = "\033[93m"
o_color = "\033[96m"
tie_color = "\033[95m"
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
signs = {"first": f"{x_color}X{normal_color}", "second": f"{o_color}O{normal_color}"}
last_sign = None


class AlreadyPlacedError(Exception):
    pass


def draw_board():
    return f"   0 | 1 | 2 \n" \
           f"0|_{board[0][0]}_|_{board[0][1]}_|_{board[0][2]}_\n" \
           f"1|_{board[1][0]}_|_{board[1][1]}_|_{board[1][2]}_\n" \
           f"2|_{board[2][0]}_|_{board[2][1]}_|_{board[2][2]}_\n\n"


def place_sign(row: int, column: int, sign: str):
    board[row][column] = sign


def clear_board():
    for row in board:
        for column in range(0, len(row)):
            row[column] = " "


def turn(sign=None):
    if sign is None or sign == signs["second"]:
        return signs["first"]
    return signs["second"]


def verify_victory():
    # Horizontals
    if board[0][0] == board[0][1] == board[0][2] and (board[0][0] != " " or board[0][1] != " " or board[0][2] != " "):
        return f"{board[0][0]} {win_color} wins! {normal_color}"
    if board[1][0] == board[1][1] == board[1][2] and (board[1][0] != " " or board[1][1] != " " or board[1][2] != " "):
        return f"{board[1][0]} {win_color} wins! {normal_color}"
    if board[2][0] == board[2][1] == board[2][2] and (board[2][0] != " " or board[2][1] != " " or board[2][2] != " "):
        return f"{board[2][0]} {win_color} wins! {normal_color}"
    # Verticals
    if board[0][0] == board[1][0] == board[2][0] and (board[0][0] != " " or board[1][0] != " " or board[2][0] != " "):
        return f"{board[0][0]} {win_color} wins! {normal_color}"
    if board[0][1] == board[1][1] == board[2][1] and (board[0][1] != " " or board[1][1] != " " or board[2][1] != " "):
        return f"{board[0][1]} {win_color} wins! {normal_color}"
    if board[0][2] == board[1][2] == board[2][2] and (board[0][2] != " " or board[1][2] != " " or board[2][2] != " "):
        return f"{board[0][2]} {win_color} wins! {normal_color}"
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and (board[0][0] != " " or board[1][1] != " " or board[2][2] != " "):
        return f"{board[0][0]} {win_color} wins! {normal_color}"
    if board[0][2] == board[1][1] == board[2][0] and (board[0][2] != " " or board[1][1] != " " or board[2][0] != " "):
        return f"{board[0][2]} {win_color} wins! {normal_color}"
    if (board[0].count(signs["first"]) + board[1].count(signs["first"]) + board[2].count(signs["first"]) +
            board[0].count(signs["second"]) + board[1].count(signs["second"]) + board[2].count(signs["second"])) == 9:
        return f"{tie_color}It's a tie!{normal_color}"
    return None


def play():
    print(ASCII_TITLE)
    sign = None
    while True:
        try:
            sign = turn(sign)
            row = int(input(f"{sign}'s turn! Choose a row to place your sign: "))
            column = int(input("Choose a column to place your sign: "))
            print(draw_board())
            if board[row][column] != " ":
                raise AlreadyPlacedError
            place_sign(row, column, sign)
            print(draw_board())
            if verify_victory() is not None:
                print(verify_victory())
                while True:
                    answer = input("Want to play again? [Y/N]\n").upper().startswith("Y")
                    if answer:
                        clear_board()
                        sign = None
                        break
                    break
                if answer is False:
                    break
        except (IndexError, ValueError):
            print(f"{error_color}Rows and Columns range from 0 to 2. Any other number will be invalid.{normal_color}")
            sign = turn(sign)
        except AlreadyPlacedError:
            print(f"{error_color}Choose only empty places.{normal_color}")
            sign = turn(sign)


play()

# There could be improvements, mainly in play function and verify_victory function.
# Also, in the future I may add a way to play against a computer instead of needing two human players.
