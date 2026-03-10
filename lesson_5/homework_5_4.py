# задание 1
matrix = [
    [1], [2], [3], [4],
    [5], [6], [7], [8],
    [9], [10], [11], [12]
]

print(matrix)
print(matrix[4:8])
print(matrix[8])

# задание 2
matrix[0:4] = [0] * len(matrix[0:4])
print(matrix)
matrix[7] = 'Python'
print(matrix)