import numpy as np

size = 9
chessboard = np.zeros((size, size), dtype=int)

for i in range(size):
    for j in range(size):
        chessboard[i, j] = (i + j) % 2

print(chessboard)