#LINk: https://leetcode.com/problems/search-a-2d-matrix/

# LeetCode 74. Search a 2D Matrix
# Time: O(log(m*n), Space: O(1)

class Solution:
    def searchInRow(self, matrix: List[List[int]], target: int, row: int) -> bool:
        n = len(matrix[0])

        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start) // 2

            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        startRow, endRow = 0, m - 1
        while startRow <= endRow:
            midRow = startRow + (endRow - startRow) // 2

            if (target >= matrix[midRow][0]) and (target <= matrix[midRow][n - 1]):
                return self.searchInRow(matrix, target, midRow)
            elif target >= matrix[midRow][n - 1]:
                startRow = midRow + 1
            else:
                endRow = midRow - 1

        return False
