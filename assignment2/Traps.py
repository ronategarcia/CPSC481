# Rodrigo Onate
# CPSC 481
# Assignment 2
# 15 Feb, 2023


from collections import deque


# check if specified row and column are valid matrix index
def isValid(i, j, N, M):
    """is Valid"""

    return (0 <= i < M) and (0 <= j < N)

# Check if current is equals 'O' and
# if it's result hasn't been changed
def isSafe(i, j, mat, result):
    """Safe move"""

    return mat[i][j] == 'O' and result[i][j] == -1

# Replace all O's in a matrix with their shortest distance
# from the nearest trap
def shortestDistanceToTraps(mat):
    """shortest distance to traps function"""

    # if mat is empty
    if not mat or not len(mat):
        return []

    # size of matrix
    M = len(mat)
    N = len(mat[0])
    result = [[0 for x in range(N)] for y in range(M)]

    # creating empty queue
    emp_queue = deque()

    # finding all the traps and appending them to queue
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 'T':
                emp_queue.append((i, j, 0))
                result[i][j] = 0
            else:
                result[i][j] = -1

    row = [0, -1, 0, 1]
    column = [-1, 0, 1, 0]

    while emp_queue:

        x_coor, y_coor, distance = emp_queue.popleft()

        for i in range(len(row)):
            if (isValid(x_coor + row[i], y_coor + column[i], N, M) and
                isSafe(x_coor + row[i], y_coor + column[i], mat, result)):

                result[x_coor + row[i]][y_coor + column[i]] = distance + 1
                emp_queue.append((x_coor + row[i], y_coor + column[i], distance + 1))

    return result

if __name__ == '__main__':

    mat = [
		['O', 'O', 'T', 'O', 'O'],
		['O', 'W', 'O', 'T', 'O'],
		['W', 'T', 'O', 'O', 'W'],
		['O', 'O', 'O', 'O', 'O']
    ]

    result = shortestDistanceToTraps(mat)

	# print results
    for r in result:
        print(r)
