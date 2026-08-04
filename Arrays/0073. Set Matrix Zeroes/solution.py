
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # get the number of rows and columns in the matrix 
        rows = len(matrix)
        cols = len(matrix[0])

        # initialize two sets to keep track of the rows and columns that need to be set to zero
        row = [False] * rows
        col = [False] * cols

        # iterate through the matrix to find the rows and columns that need to be set to zero
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        # iterate through the matrix again to set the rows and columns to zero
        for i in range(rows):   
            for j in range(cols):
                if row[i] or col[j]:
                    matrix[i][j] = 0


#-------------------------main Program--------------------
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix)
    print(matrix)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
