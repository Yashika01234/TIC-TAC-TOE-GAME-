from game import TicTacToe
from ai import best_move

game = TicTacToe()

print("AI Tic Tac Toe")
print("You are X")
print()

while game.empty_squares():

    game.print_board()

    try:
        move = int(input("Enter position (0-8): "))

        if not game.make_move(move, "X"):
            print("Invalid Move")
            continue

        if game.winner(move, "X"):
            game.print_board()
            print("You Win!")
            break

        if not game.empty_squares():
            print("Draw!")
            break

        ai_move = best_move(game.board)

        game.make_move(ai_move, "O")

        print(f"AI chose {ai_move}")

        if game.winner(ai_move, "O"):
            game.print_board()
            print("AI Wins!")
            break

    except:
        print("Enter valid number")