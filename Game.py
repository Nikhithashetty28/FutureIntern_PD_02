def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows, columns and diagonals for a winner
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, enter your move (row and column): ")

        while True:
            try:
                row, col = map(int, input().split())
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell already taken! Choose another one.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter row and column (0-2): ")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break


if __name__ == "__main__":
    main()

