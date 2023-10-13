import random
def print_board(board):
    print(" ".join(board[:3]))
    print(" ".join(board[3:6]))
    print(" ".join(board[6:]))
def open_slots(board):
    ans=[]
    for i in range(len(board)):
        if board[i]=="-":
            ans.append(i)
    return ans
def random_move(board, symbol):
    board[random.choice(open_slots(board))]=symbol
    print_board(board)
def random_move2(board, symbol):
    board[random.choice(open_slots(board))]=symbol
    return board
def check_three(board, idx1, idx2, idx3):
    if (board[idx1]==board[idx2]==board[idx3]) and (board[idx1]!='-'):
        return board[idx1]
    return "-"
def winner(board):
    poss=[check_three(board, 0, 1, 2),check_three(board, 3, 4, 5),check_three(board, 6, 7, 8),check_three(board, 0, 3, 6),check_three(board, 1, 4, 7),check_three(board, 2, 5, 8),check_three(board, 0, 4, 8),check_three(board, 2, 4, 6)]
    for i in poss:
        if i in ['X', 'O']:
            return i
    if '-' in board:
        return '-'
    else:
        return 'D'
def hundred_games():
    X=O=D=0
    for _ in range(100):
        board=['-' for _ in range(9)]
        while '-' in board:
            board=random_move2(board, random.choice(['X', 'O']))
        if winner(board)=='X':
            X+=1
        elif winner(board)=='O':
            O+=1
        elif winner(board)=='D':
            D+=1
    return f'X wins: {X}\nO wins: {O}\nDraws: {D}'