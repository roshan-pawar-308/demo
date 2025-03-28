# 8. Matrix Manipulation (Transpose a Matrix)
# ✅ Task: Write a function to find the transpose of a given matrix.
#  🔹 Requirements:
# A transpose swaps rows and columns.


# python
# CopyEdit
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in 
    range(len(matrx))] for i in 
    range(len(matrix[1]))]
     

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transpose_matrix(matrix))
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]