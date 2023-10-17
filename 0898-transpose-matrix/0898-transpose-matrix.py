class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposeMatrix = [[0 for row in range(len(matrix))] for coloum in range(len(matrix[0]))]
        for coloum in range(len(matrix)):
            for row in range(len(matrix[0])):
                transposeMatrix[row][coloum] = matrix[coloum][row]

        return transposeMatrix