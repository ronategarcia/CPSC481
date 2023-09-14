# Rodrigo Onate
# CPSC 481
# Assignment 2
# 15 Feb, 2023


# Below lists detail all eight possible movements from a cell
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# Function to check if it is possible to go to position next
# from the current position. The function returns false if next is
# not in a valid position, or it is already visited
def isValid(mat, x, y, path):
	return (0 <= x < len(mat)) and (0 <= y < len(mat[0])) and (x, y) not in path


def DFS(mat, word, i, j, path=[], index=0):
	# Check if the first character of the word matches
	# the current character from mat
	if mat[i][j] != word[index]:
		return
	
	# Appending current character in mat to the path list
	path.append((word[index], i, j))

	# Printing path 
	if index == len(word) - 1:
		print(path)
	else:
		for p in range(len(row)):
			if isValid(mat, i + row[p], j + col[p], path):
				DFS(mat, word, i + row[p], j + col[p], path, index + 1)

	path.pop()


def WordSearch(mat, word):
	# base case
	if not mat or not len(mat) or not len(word):
		return

	for i in range(len(mat)):
		for j in range(len(mat[0])):
			DFS(mat, word, i, j)


if __name__ == '__main__':

	mat = [
		['A', 'D', 'E', 'B', 'C'],
		['O', 'O', 'C', 'A', 'X'],
		['S', 'C', 'D', 'K', 'C'],
		['O', 'D', 'E', 'H', 'L']
	]
	word = 'CODE'

	WordSearch(mat, word)
