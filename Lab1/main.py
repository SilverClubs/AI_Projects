from math import sqrt
from copy import deepcopy

goal = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
]


def compress(arr):
    num = 0
    i = 0
    for row in range(2, -1, -1):
        for col in range(2, -1, -1):
            num += arr[row][col] * pow(10, i)
            i += 1
    return num


def decompress(num):
    arr = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    end = False
    for row in range(2, -1, -1):
        for col in range(2, -1, -1):
            rem = int(num % 10)
            arr[row][col] = rem
            num = int(num / 10)
            if num == 0:
                end = True
                break
        if end:
            break
    return arr


def get_row_col(key, arr):
    for row in range(3):
        for col in range(3):
            if key == arr[row][col]:
                return (row, col)
    return -1


def manhattan(cur_state):
    total = 0
    for row in range(3):
        for col in range(3):
            key = goal[row][col]
            row, col = get_row_col(key, goal)
            cur_row, cur_col = get_row_col(key, cur_state)
            total += abs(row - cur_row) + abs(col - cur_col)
    return total


def euclidean(cur_state):
    total = 0
    for row in range(3):
        for col in range(3):
            key = goal[row][col]
            row, col = get_row_col(key, goal)
            cur_row, cur_col = get_row_col(key, cur_state)
            total += sqrt(pow(row - cur_row, 2) + pow(col - cur_col, 2))
    return total


def goal_check(cur_state):
    return cur_state == goal


def expand(cur_state):  # returns compressed states
    states = []
    row, col = get_row_col(0, cur_state)
    if row > 0:  # move up
        temp = deepcopy(cur_state)
        temp[row][col], temp[row - 1][col] = temp[row - 1][col], temp[row][col]
        states.append(compress(temp))
    if row < 2:  # move down
        temp = deepcopy(cur_state)
        temp[row][col], temp[row + 1][col] = temp[row + 1][col], temp[row][col]
        states.append(compress(temp))
    if col > 0:  # move left
        temp = deepcopy(cur_state)
        temp[row][col], temp[row][col - 1] = temp[row][col - 1], temp[row][col]
        states.append(compress(temp))
    if col < 2:  # move right
        temp = deepcopy(cur_state)
        temp[row][col], temp[row][col + 1] = temp[row][col + 1], temp[row][col]
        states.append(compress(temp))
    return states
