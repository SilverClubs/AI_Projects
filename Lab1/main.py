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
