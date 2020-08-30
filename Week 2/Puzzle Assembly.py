# python3
import math
import numpy as np
from copy import deepcopy
from pprint import pprint

DATA_COUNT = 25

'''
up: 0
left: 1
down: 2
right: 3
'''
direction = {'up': 0, 'left': 1, 'down': 2, 'right': 3}
is_checked = np.array([])
matrix = []


def read_input():
    data = []
    for i in range(DATA_COUNT):
        data.append(input())
    n = int(math.sqrt(len(data)))
    blocks = []
    for d in data:
        blocks.append(d[1:-1].split(','))
    return n, blocks


def print_matrix(matrix, n):
    result = []
    for i in range(n):
        res = ""
        for j in range(n):
            res += "("
            for k in range(4):
                res += matrix[i][j][k]
                res += ','
            res = res[:-1]
            res += ')'
            res += ';'
        res = res[:-1]
        result.append(res)
    for r in result:
        print(r)


def find_corners(data, n):
    global is_checked, matrix
    data = np.array(data)
    for i, d in enumerate(data):
        if d[0] == 'black' and d[1] == 'black':
            matrix[0][0] = d
            is_checked[i] = True
        elif d[1] == 'black' and d[2] == 'black':
            matrix[n - 1][0] = d
            is_checked[i] = True
        elif d[2] == 'black' and d[3] == 'black':
            matrix[n - 1][n - 1] = d
            is_checked[i] = True
        elif d[3] == 'black' and d[0] == 'black':
            matrix[0][n - 1] = d
            is_checked[i] = True


def find_up_side(data, i=1):
    global is_checked, direction, matrix
    matrix_copy = deepcopy(matrix)
    if i >= math.sqrt(DATA_COUNT) - 1:
        return True

    if i == math.sqrt(DATA_COUNT) - 2:
        for d in data:
            if d[0][direction['left']] == matrix[0][i - 1][direction['right']] and d[0][direction['right']] == \
                    matrix[0][i + 1][direction['left']]:
                matrix[0][i] = d[0]
                is_checked[d[1]] = True
                return True
        return False

    for d in data:
        if d[0][direction['left']] == matrix[0][i - 1][direction['right']]:
            matrix[0][i] = d[0]
            is_checked[d[1]] = True
            f = find_up_side(data, i + 1)
            if not f:
                matrix = matrix_copy
                is_checked[d[1]] = False
                continue
            else:
                return True


def find_left_side(data, i=1):
    global is_checked, direction, matrix
    matrix_copy = deepcopy(matrix)
    if i > math.sqrt(DATA_COUNT) - 1:
        return True

    if i == math.sqrt(DATA_COUNT) - 2:
        for d in data:
            if d[0][direction['up']] == matrix[i - 1][0][direction['down']] and d[0][direction['down']] == \
                    matrix[i + 1][0][direction['up']]:
                matrix[i][0] = d[0]
                is_checked[d[1]] = True
                return True
        return False

    for d in data:
        if d[0][direction['up']] == matrix[i - 1][0][direction['down']]:
            matrix[i][0] = d[0]
            is_checked[d[1]] = True
            f = find_left_side(data, i + 1)
            if not f:
                matrix = matrix_copy
                is_checked[d[1]] = False
                continue
            else:
                return True


def find_down_side(data, i=1):
    global is_checked, direction, matrix
    matrix_copy = deepcopy(matrix)
    if i > math.sqrt(DATA_COUNT) - 1:
        return True

    if i == math.sqrt(DATA_COUNT) - 2:
        for d in data:
            if d[0][direction['left']] == matrix[-1][i - 1][direction['right']] and d[0][direction['right']] == \
                    matrix[-1][i + 1][direction['left']]:
                matrix[-1][i] = d[0]
                is_checked[d[1]] = True
                return True
        return False

    for d in data:
        if d[0][direction['left']] == matrix[-1][i - 1][direction['right']]:
            matrix[-1][i] = d[0]
            is_checked[d[1]] = True
            f = find_down_side(data, i + 1)
            if not f:
                matrix = matrix_copy
                is_checked[d[1]] = False
                continue
            else:
                return True


def find_right_side(data, i=1):
    global is_checked, direction, matrix
    matrix_copy = deepcopy(matrix)

    if i > math.sqrt(DATA_COUNT) - 1:
        return True

    if i == math.sqrt(DATA_COUNT) - 2:
        for d in data:
            if d[0][direction['up']] == matrix[i - 1][-1][direction['down']] and d[0][direction['down']] == \
                    matrix[i + 1][-1][direction['up']]:
                matrix[i][-1] = d[0]
                is_checked[d[1]] = True
                return True
        return False

    for d in data:
        if d[0][direction['up']] == matrix[i - 1][-1][direction['down']]:
            matrix[i][-1] = d[0]
            is_checked[d[1]] = True
            f = find_right_side(data, i + 1)
            if not f:
                matrix = matrix_copy
                is_checked[d[1]] = False
                continue
            else:
                return True


def find_centers(data, i=1, j=1):
    global is_checked, direction, matrix
    matrix_copy = deepcopy(matrix)
    for d in data:
        if i == math.sqrt(DATA_COUNT) - 2 and j == math.sqrt(DATA_COUNT) - 2:
            if d[0][direction['up']] == matrix[i - 1][j][direction['down']] and \
                    d[0][direction['left']] == matrix[i][j - 1][direction['right']] and \
                    d[0][direction['right']] == matrix[i][j + 1][direction['left']] and \
                    d[0][direction['down']] == matrix[i + 1][j][direction['up']]:
                matrix[i][j] = d[0]
                is_checked[d[1]] = True
                return True
        elif i == math.sqrt(DATA_COUNT) - 2:
            if d[0][direction['up']] == matrix[i - 1][j][direction['down']] and \
                    d[0][direction['down']] == matrix[i + 1][j][direction['up']] and \
                    d[0][direction['left']] == matrix[i][j - 1][direction['right']]:
                matrix[i][j] = d[0]
                is_checked[d[1]] = True
                f = find_centers(data, i, j + 1)
                if not f:
                    matrix = matrix_copy
                    is_checked[d[1]] = False
                else:
                    return True
        elif j == math.sqrt(DATA_COUNT) - 2:
            if d[0][direction['up']] == matrix[i - 1][j][direction['down']] and \
                    d[0][direction['right']] == matrix[i][j + 1][direction['left']] and \
                    d[0][direction['left']] == matrix[i][j - 1][direction['right']]:
                matrix[i][j] = d[0]
                is_checked[d[1]] = True
                f = find_centers(data, i + 1, 1)
                if not f:
                    matrix = matrix_copy
                    is_checked[d[1]] = False
                else:
                    return True
        else:
            if d[0][direction['up']] == matrix[i - 1][j][direction['down']] and \
                    d[0][direction['left']] == matrix[i][j - 1][direction['right']]:
                matrix[i][j] = d[0]
                is_checked[d[1]] = True
                f = find_centers(data, i, j + 1)
                if not f:
                    matrix = matrix_copy
                    is_checked[d[1]] = False
                else:
                    return True
    return False


def extract_sides(data, side):
    global is_checked
    sides = []
    for i, d in enumerate(data):
        if is_checked[i]:
            continue
        if d[direction[side]] == 'black':
            sides.append((d, i))
    return sides


def extract_center(data):
    centers = []
    for i, d in enumerate(data):
        if 'black' in d:
            continue
        centers.append((d, i))
    return centers


if __name__ == '__main__':
    n, blocks = read_input()
    is_checked = np.full((n ** 2), [False])
    matrix = np.ndarray((n, n, 4), dtype=object)
    find_corners(blocks, n)
    up = extract_sides(blocks, 'up')
    down = extract_sides(blocks, 'down')
    left = extract_sides(blocks, 'left')
    right = extract_sides(blocks, 'right')
    center = extract_center(blocks)
    find_up_side(up)
    find_down_side(down)
    find_left_side(left)
    find_right_side(right)
    find_centers(center)
    print_matrix(matrix,n)
    # pprint(matrix)
    # print(up)
    # print(left)
    # print(down)
    # print(right)
    # print(center)

'''
(yellow,black,black,blue)
(blue,blue,black,yellow)
(orange,yellow,black,black)
(red,black,yellow,green)
(orange,green,blue,blue)
(green,blue,orange,black)
(black,black,red,red)
(black,red,orange,purple)
(black,purple,green,black)
'''

'''
(yellow,purple,black,green)
(orange,green,black,purple)
(black,green,red,black)
(purple,green,orange,green)
(green,green,purple,black)
(black,red,green,green)
(green,red,red,red)
(red,red,purple,orange)
(purple,red,black,black)
(yellow,green,purple,orange)
(yellow,black,orange,red)
(purple,green,yellow,green)
(red,black,yellow,red)
(green,purple,yellow,green)
(orange,orange,green,black)
(purple,red,red,purple)
(red,orange,purple,green)
(red,green,orange,black)
(orange,black,green,green)
(orange,purple,black,red)
(green,black,black,purple)
(black,yellow,green,orange)
(purple,green,orange,green)
(black,black,red,yellow)
(black,orange,purple,red)
'''