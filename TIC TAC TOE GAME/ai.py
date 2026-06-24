def minimax(board, maximizing):

    winner = check_winner(board)

    if winner == "O":
        return 1

    if winner == "X":
        return -1

    if " " not in board:
        return 0

    if maximizing:
        best_score = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


def check_winner(board):

    winning_positions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for combo in winning_positions:

        a,b,c = combo

        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


def best_move(board):

    best_score = -100
    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move