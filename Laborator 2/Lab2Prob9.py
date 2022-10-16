def dontseegame(m):
    listspect = []
    for i in range(1, len(m)):
        for j in range(0, len(m[0])):
            for k in range(0, i):
                if m[k][j] >= m[i][j]:
                    listspect.append((i, j))
                    break

    return listspect


if __name__ == '__main__':
    print(dontseegame([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))
