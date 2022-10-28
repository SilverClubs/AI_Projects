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
    goal = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
    total = 0
    for row in range(3):
        for col in range(3):
            key = goal[row][col]
            row, col = get_row_col(key, goal)
            cur_row, cur_col = get_row_col(key, cur_state)
            total += abs(row - cur_row) + abs(col - cur_col)
    return total
