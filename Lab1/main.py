from math import sqrt
from copy import deepcopy
from queue import PriorityQueue
import time


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


def a_star(initial_state, heuristic):
    parent_map = {}
    parent_map[compress(initial_state)] = compress(initial_state)
    frontier = PriorityQueue()
    frontier.put((heuristic(initial_state), compress(initial_state)))
    frontier_map = {}
    frontier_map[compress(initial_state)] = heuristic(initial_state)
    explored = set()
    expanded_count = 0

    while not frontier.empty():
        state = frontier.get()
        h = heuristic(decompress(state[1]))
        g = state[0] - h
        state = state[1]
        explored.add(state)
        state = decompress(state)
        if goal_check(state):
            return (True, expanded_count, parent_map)

        neighbors = expand(state)
        state = compress(state)
        expanded_count += 1
        for neighbor in neighbors:
            if neighbor not in explored:
                cost = g + 1 + heuristic(decompress(neighbor))
                if neighbor not in frontier_map or cost < frontier_map[neighbor]:
                    frontier.put((cost, neighbor))
                    frontier_map[neighbor] = cost
                    parent_map[neighbor] = state

    return (False, expanded_count, parent_map)


def get_path_depth(parent_map):
    path = []
    node = compress(goal)
    if node in parent_map:
        parent = parent_map[node]
        while node != parent:
            path.append(node)
            node = parent
            parent = parent_map[node]
        path.append(node)

    cost_map = {}
    for node in parent_map:
        parent = parent_map[node]
        tmp = [node]
        while node != parent and node not in cost_map:
            node = parent
            parent = parent_map[node]
            tmp.append(node)

        cost = len(tmp) - 1
        if node in cost_map:
            cost += cost_map[node]

        for node in tmp:
            if node in cost_map:
                break
            cost_map[node] = cost
            cost -= 1

    return (len(path) - 1, path, cost_map[max(cost_map, key=cost_map.get)])


initial = [
    [1, 2, 5],
    [3, 4, 8],
    [6, 7, 0],
]

unsolvable_state = [
    [8, 1, 2],
    [0, 4, 3],
    [7, 6, 5],
]

test = [
    [1, 8, 2],
    [0, 4, 3],
    [7, 6, 5],
]

start = time.time()
success, expanded_count, parent_map = a_star(test, manhattan)
end = time.time()
print(f"Elapsed time: {end-start} seconds")
print(f"Nodes expanded: {expanded_count}")
cost, path, depth = get_path_depth(parent_map)
print(f"Search depth: {depth}")
if success:
    print(f"Path found. Cost: {cost}.")
    print(f"Path: {path}")
else:
    print(f"Path not found.")
