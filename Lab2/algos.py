# 1 is ai
# 2 is human

import functools
import treelib
import uuid

# From gui to algos
def swaparr(arr):
    board = [
        # 0,1,2,3,4,5,6
        [0, 0, 0, 0, 0, 0, 0],  # row 1
        [0, 0, 0, 0, 0, 0, 0],  # row 2
        [0, 0, 0, 0, 0, 0, 0],  # row 3
        [0, 0, 0, 0, 0, 0, 0],  # row 4
        [0, 0, 0, 0, 0, 0, 0],  # row 5
        [0, 0, 0, 0, 0, 0, 0],  # row 6
    ]

    for i in range(7):
        for j in range(6):
            board[j][i] = arr[i][j]

    return board


# From algos to gui
def swaparr2(arr):
    board = [
        # 0,1,2,3,4,5,6
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    for i in range(6):
        for j in range(7):
            board[j][i] = arr[i][j]

    return board


weights = [  # max value is 62
    [2, 3, 7, 7, 3, 2],
    [3, 6, 7, 7, 6, 3],
    [4, 6, 9, 9, 6, 4],
    [4, 6, 9, 9, 6, 4],
    [3, 6, 7, 7, 6, 3],
    [2, 3, 7, 7, 3, 2],
]


def heuristic(int_board):
    total = score(int_board) - 1
    board = extra_expand(expand(int_board))
    board = [[-1 if x == 2 else x for x in row] for row in board]
    board = [[x * y for x, y in zip(b, w)] for b, w in zip(board, weights)]
    w = sum(sum(board, []))  # max weight is 62
    w = w / 62
    total += w

    return total


def comp_heuristic(board1, board2):
    return heuristic(board1) - heuristic(board2)


def expand(int_board):  # returns an array were each slot represents a
    board_state = format(int_board, "063b")
    i = 0
    j = 0
    filled = ["" for x in range(7)]
    while i <= 54:
        filled[j] = board_state[i : i + 9]
        j = j + 1
        i = i + 9

    return filled


def extra_expand(coloumns):
    board = [
        # 0,1,2,3,4,5,6
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    i = 0
    for coloumn in coloumns:
        f_empty = int(coloumn[0:3], 2)
        last_bit = 9

        for j in range(5, f_empty - 1, -1):
            board[j][i] = 2 - ord(coloumn[last_bit - 1]) + 48
            last_bit = last_bit - 1
        i = i + 1
    return board


def compress(board):
    filled = ["" for x in range(7)]
    for i in range(6, -1, -1):
        col_position = 0
        for j in range(5, -1, -1):
            if j == 0:
                if board[j][i] == 0:
                    col_position = j + 1
                    if filled[i] != "":
                        col_position = format(col_position, "03b")
                        filled[i] = format(int(filled[i], 2), "06b")
                        filled[i] = col_position + filled[i]
                    else:
                        filled[i] = format(col_position, "03b") + "000000"

                    break
                elif board[j][i] == 1:
                    filled[i] = format(0, "03b") + format(1, "01b") + filled[i]
                elif board[j][i] == 2:
                    filled[i] = format(0, "03b") + format(0, "01b") + filled[i]

            elif board[j][i] == 0:
                col_position = j + 1
                if filled[i] != "":
                    col_position = format(col_position, "03b")
                    filled[i] = format(int(filled[i], 2), "06b")
                    filled[i] = col_position + filled[i]
                else:
                    filled[i] = format(col_position, "03b") + "000000"
                break
            elif board[j][i] == 1:
                filled[i] = format(1, "01b") + filled[i]
            elif board[j][i] == 2:
                filled[i] = format(0, "01b") + filled[i]

    return filled


def extra_compress(board):
    filled = compress(board)
    temp = ""
    for f in filled:
        temp = temp + f
    int_board = int(temp, 2)
    return int_board


def place(int_board, col):  # the coloum where the player wants to add a piece
    coloums = expand(int_board)
    coloum = coloums[col]
    first_empty = coloum[0:3]
    f_empty = int()


def is_goal(int_board):
    return (
        int_board & 0b111000000111000000111000000111000000111000000111000000111000000
    ) == 0


def minimize(int_board, depth, tree, parentID):
    pID = uuid.uuid1()
    tree.create_node(int_board, pID, parent=parentID)
    if is_goal(int_board):
        return score(int_board), int_board
    if depth == 0:
        return heuristic(int_board), int_board
    neighbours = explore(int_board, 2)
    best_move = 100000000
    best_neighbour = 0
    for neighbour in neighbours:
        move = maximize(neighbour, depth - 1, tree, pID)
        if move[0] < best_move:
            best_move = move[0]
            best_neighbour = neighbour
    return best_move, best_neighbour


def maximize(int_board, depth, tree, parentID):
    pID = uuid.uuid1()
    tree.create_node(int_board, pID, parent=parentID)
    if is_goal(int_board):
        return score(int_board), int_board
    if depth == 0:
        return heuristic(int_board), int_board
    neighbours = explore(int_board, 1)
    best_move = -100000000
    best_neighbour = 0
    for neighbour in neighbours:
        move = minimize(neighbour, depth - 1, tree, pID)
        if move[0] > best_move:
            best_move = move[0]
            best_neighbour = neighbour
    return best_move, best_neighbour


def minimize_beta(int_board, depth, alpha, beta, tree, parentID):
    pID = uuid.uuid1()
    tree.create_node(int_board, pID, parent=parentID)
    if is_goal(int_board):
        return score(int_board), int_board
    if depth == 0:
        return heuristic(int_board), int_board
    neighbours = explore(int_board, 2)
    best_move = 100000000
    best_neighbour = 0
    for neighbour in neighbours:
        move = maximize_alpha(neighbour, depth - 1, alpha, beta, tree, pID)
        if move[0] < best_move:
            best_move = move[0]
            best_neighbour = neighbour
        if move[0] <= alpha:
            break
        if move[0] < beta:
            beta = move[0]

    return best_move, best_neighbour


def maximize_alpha(int_board, depth, alpha, beta, tree, parentID):
    pID = uuid.uuid1()
    tree.create_node(int_board, pID, parent=parentID)
    if is_goal(int_board):
        return score(int_board), int_board
    if depth == 0:
        return heuristic(int_board), int_board
    neighbours = explore(int_board, 1)
    best_move = -100000000
    best_neighbour = 0
    for neighbour in neighbours:
        move = minimize_beta(neighbour, depth - 1, alpha, beta, tree, pID)
        if move[0] > best_move:
            best_move = move[0]
            best_neighbour = neighbour
        if move[0] >= beta:
            break
        if move[0] > alpha:
            alpha = move[0]
    return best_move, best_neighbour


def explore(int_board, turn):
    states = []
    empty = []
    cols = expand(int_board)
    board = extra_expand(cols)
    i = 0
    if turn == 1:
        i = 0
        for col in cols:
            first_empty = col[0:3]
            f_empty = int(first_empty, 2)
            tempboard = [row[:] for row in board]
            if f_empty != 0:
                tempboard[f_empty - 1][i] = 1
                states.append(extra_compress(tempboard))
            i = i + 1

    elif turn == 2:
        i = 0
        for col in cols:
            first_empty = col[0:3]
            f_empty = int(first_empty, 2)
            tempboard = [row[:] for row in board]
            if f_empty != 0:
                tempboard[f_empty - 1][i] = 2
                states.append(extra_compress(tempboard))
            i = i + 1
    return states


def score(int_board):
    cols = expand(int_board)
    board = extra_expand(cols)
    scoreai = 0
    scorehi = 0
    for i in range(6):  # loops row by row
        for j in range(4):
            if (
                board[i][j] == 1
                and board[i][j + 1] == 1
                and board[i][j + 2] == 1
                and board[i][j + 3] == 1
            ):
                scoreai = scoreai + 1
            elif (
                board[i][j] == 2
                and board[i][j + 1] == 2
                and board[i][j + 2] == 2
                and board[i][j + 3] == 2
            ):
                scorehi = scorehi + 1

    for i in range(7):  # loops column by column
        for j in range(3):
            if (
                board[j + 3][i] == 1
                and board[j + 2][i] == 1
                and board[j + 1][i] == 1
                and board[j][i] == 1
            ):
                scoreai = scoreai + 1
            elif (
                board[j + 3][i] == 2
                and board[j + 2][i] == 2
                and board[j + 1][i] == 2
                and board[j][i] == 2
            ):
                scorehi = scorehi + 1

    for i in range(3):  # bottom left top right diagonals
        for j in range(4):
            if (
                board[i + 3][j + 3] == 1
                and board[i + 2][j + 2] == 1
                and board[i + 1][j + 1] == 1
                and board[i][j] == 1
            ):
                scoreai = scoreai + 1
            elif (
                board[i + 3][j + 3] == 2
                and board[i + 2][j + 2] == 2
                and board[i + 1][j + 1] == 2
                and board[i][j] == 2
            ):
                scorehi = scorehi + 1

    for i in range(3):  # bottom right top left diagonals
        for j in range(3, 7):
            if (
                board[i + 3][j - 3] == 1
                and board[i + 2][j - 2] == 1
                and board[i + 1][j - 1] == 1
                and board[i][j] == 1
            ):
                scoreai = scoreai + 1
            elif (
                board[i + 3][j - 3] == 2
                and board[i + 2][j - 2] == 2
                and board[i + 1][j - 1] == 2
                and board[i][j] == 2
            ):
                scorehi = scorehi + 1

    score_diff = scoreai - scorehi
    return score_diff


def scoregui(int_board):
    cols = expand(int_board)
    board = extra_expand(cols)
    scoreai = 0
    scorehi = 0
    for i in range(6):  # loops row by row
        for j in range(4):
            if (
                board[i][j] == 1
                and board[i][j + 1] == 1
                and board[i][j + 2] == 1
                and board[i][j + 3] == 1
            ):
                scoreai = scoreai + 1
            elif (
                board[i][j] == 2
                and board[i][j + 1] == 2
                and board[i][j + 2] == 2
                and board[i][j + 3] == 2
            ):
                scorehi = scorehi + 1

    for i in range(7):  # loops column by column
        for j in range(3):
            if (
                board[j + 3][i] == 1
                and board[j + 2][i] == 1
                and board[j + 1][i] == 1
                and board[j][i] == 1
            ):
                scoreai = scoreai + 1
            elif (
                board[j + 3][i] == 2
                and board[j + 2][i] == 2
                and board[j + 1][i] == 2
                and board[j][i] == 2
            ):
                scorehi = scorehi + 1

    for i in range(3):  # bottom left top right diagonals
        for j in range(4):
            if (
                board[i + 3][j + 3] == 1
                and board[i + 2][j + 2] == 1
                and board[i + 1][j + 1] == 1
                and board[i][j] == 1
            ):
                scoreai = scoreai + 1
            elif (
                board[i + 3][j + 3] == 2
                and board[i + 2][j + 2] == 2
                and board[i + 1][j + 1] == 2
                and board[i][j] == 2
            ):
                scorehi = scorehi + 1

    for i in range(3):  # bottom right top left diagonals
        for j in range(3, 7):
            if (
                board[i + 3][j - 3] == 1
                and board[i + 2][j - 2] == 1
                and board[i + 1][j - 1] == 1
                and board[i][j] == 1
            ):
                scoreai = scoreai + 1
            elif (
                board[i + 3][j - 3] == 2
                and board[i + 2][j - 2] == 2
                and board[i + 1][j - 1] == 2
                and board[i][j] == 2
            ):
                scorehi = scorehi + 1

    return scorehi, scoreai


if __name__ == "__main__":

    board = [
        # 0,1,2,3,4,5,6
        [0, 0, 0, 0, 0, 0, 0],  # row 1
        [0, 0, 0, 0, 0, 0, 0],  # row 2
        [0, 0, 0, 0, 0, 0, 0],  # row 3
        [0, 0, 0, 0, 0, 0, 0],  # row 4
        [2, 1, 2, 1, 2, 1, 2],  # row 5
        [1, 2, 1, 2, 1, 2, 1],  # row 6
    ]

    f = extra_compress(board)

    t = treelib.Tree()
    move = maximize(f, 6, t, None)
    newboard = move[1]
    newcols = expand(newboard)
    newf = extra_expand(newcols)
    for i in range(6):
        print(newf[i])
