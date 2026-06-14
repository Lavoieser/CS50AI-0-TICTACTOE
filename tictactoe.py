"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = 0
    O_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                X_count += 1
            elif board[i][j] == O:
                O_count += 1

    if X_count <= O_count:  
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.append((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    play = player(board)
    i = action[0]
    j = action[1]    
    board[i][j] = play
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win = utility(board)
    if win == 1:
        return "X"
    elif win == -1:
        return "O"
    else:
        return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    X_count = sum(row.count("X") for row in board)
    O_count = sum(row.count("O") for row in board)
    total_played = X_count + O_count

    win = utility(board)

    if (win == 1 or win == -1 or total_played == 9):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Check lines
    for i in range(3):
        if board[i].count("X") == 3:
            return 1
        elif board[i].count("O") == 3:
            return -1
        
    # check columns
    for j in range(3):
        X_count = 0
        O_count = 0
        for i in range(3):
            if board[i][j] == "X":
                X_count +=1
            elif board[i][j] == "O":
                O_count += 1

        if X_count == 3:
            return 1
        elif O_count == 3:
            return -1
            
    # Check diagonals
    X_count = 0
    O_count = 0
    for i in range(3):
        if board[i][i] == "X":
            X_count +=1
        elif board[i][i] == "O":
            O_count += 1

    if X_count == 3:
        return 1
    elif O_count == 3:            
        return -1
            
    X_count = 0
    O_count = 0
    for j in range(3):
        i = 2 - j
        if board[i][j] == "X":
            X_count +=1
        if board[i][j] == "O":
            O_count += 1

    if X_count == 3:
        return 1
    elif O_count == 3:            
        return -1
    
    # If there is no winner yet
    return 0

    
def priority_move(actions):
    priority = {
        (1, 1): 1,
        (0, 0): 2,
        (0, 2): 3,
        (2, 0): 4,
        (2, 2): 5
    }
    ordered_actions = sorted(actions, key=lambda a: priority.get(a, 99))
    return (ordered_actions)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    """
    if terminal(board):
        return None

    current_player = player(board)
    actions_ordered = priority_move(actions(board))

    if current_player == X:
        best_score = -math.inf
        best_move = None
        for action in actions_ordered:
            new_board = [row.copy() for row in board]
            new_board = result(new_board, action)
            score = minimax_score(new_board, False)
            if score > best_score:
                best_score = score
                best_move = action
        return best_move
    else:  # current_player == O
        best_score = math.inf
        best_move = None
        for action in actions_ordered:
            new_board = [row.copy() for row in board]
            new_board = result(new_board, action)
            score = minimax_score(new_board, True)
            if score < best_score:
                best_score = score
                best_move = action
        return best_move
    
def minimax_score(board, is_maximizing):
    if terminal(board):
        return utility(board)

    if is_maximizing:
        best_score = -math.inf
        for action in actions(board):
            new_board = [row.copy() for row in board]
            new_board = result(new_board, action)
            score = minimax_score(new_board, False)
            best_score = max(score, best_score)
        return best_score

    else:  # minimizing player
        best_score = math.inf
        for action in actions(board):
            new_board = [row.copy() for row in board]
            new_board = result(new_board, action)
            score = minimax_score(new_board, True)
            best_score = min(score, best_score)
        return best_score
