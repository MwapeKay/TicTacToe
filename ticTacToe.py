board = [" " for x in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player {}".format(number))

    while True:
        try:
            choice = int(input("Enter your move (1-9): ").strip())
            if choice < 1 or choice > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            if board[choice - 1] == " ":
                board[choice - 1] = icon
                break
            else:
                print("That space is taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def is_victory(icon):
    return ((board[0] == icon and board[1] == icon and board[2] == icon) or
            (board[3] == icon and board[4] == icon and board[5] == icon) or
            (board[6] == icon and board[7] == icon and board[8] == icon) or
            (board[0] == icon and board[3] == icon and board[6] == icon) or
            (board[1] == icon and board[4] == icon and board[7] == icon) or
            (board[2] == icon and board[5] == icon and board[8] == icon) or
            (board[0] == icon and board[4] == icon and board[8] == icon) or
            (board[2] == icon and board[4] == icon and board[6] == icon))

def is_draw():
    return " " not in board

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    print_board()
    if is_victory("O"):
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break

