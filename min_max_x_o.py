def print_board(board):
    for row in board:
        print(row)


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None


def is_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'x':
        return -1
    if winner == 'o':
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'o'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'x'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score


def best_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'o'
                score = minimax(board, 0, False)
                board[i][j] = ' '  # Reset the board after checking
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if board[best_move[0]][best_move[1]] == ' ':
        return best_move
    else:
        return None


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    first_move = input('Who goes first? (x/o): ')
    while True:
        if first_move == 'x':
            x, y = map(int, input('Enter your move: ').split())
            if board[x][y] == ' ':
                board[x][y] = 'x'
            else:
                print('Invalid move')
                continue
            if check_winner(board) == 'x':
                print('You win!')
                break
            if is_full(board):
                print('Draw!')
                break
            first_move = 'o'
        if first_move == 'o':
            x, y = best_move(board)
            if x is None and y is None:
                print('Draw!')
                break
            board[x][y] = 'o'
            print_board(board)
            if check_winner(board) == 'o':
                print('You lose!')
                break
            if is_full(board):
                print('Draw!')
                break
            first_move = 'x'


if __name__ == '__main__':
    main()
