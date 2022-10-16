# Write a function that receives as parameter a matrix and will return the matrix
# obtained by replacing all the elements under the main diagonal with 0 (zero)

def matrix(m):
    for j in range(len(m)):
        for i in range(j+1, len(m)):
            m[i][j] = 0
    return m


if __name__ == '__main__':
    print(matrix([[12, 6, 1, 19], [5, 8, 91, 0], [15, 27, 11, 7], [1, 23, 4, 37]]))
