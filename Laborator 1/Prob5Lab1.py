def spiral_matrix(matrix):
    top = 0
    down = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    text = []
    while top <= down and left <= right:
        for i in range(left, right + 1):
            text.append(matrix[top][i])
        top += 1
        for i in range(top, down + 1):
            text.append(matrix[i][right])
        right -= 1
        for i in range(right, left - 1, -1):
            text.append(matrix[down][i])
        down -= 1
        for i in range(down, top - 1, -1):
            text.append(matrix[i][left])
        left += 1
    return ''.join(text)


if __name__ == '__main__':
    print(spiral_matrix([['f', 'i', 'r', 's'], ['n', '_', 'l', 't'], ['o', 'b', 'a', '_'], ['h', 't', 'y', 'p']]))
