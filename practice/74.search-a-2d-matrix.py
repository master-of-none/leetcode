# @leet start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top = 0
        bot = ROWS-1

        while top <= bot:
            mid = (top + bot) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break

        row = (top + bot) // 2
        l = 0
        r = COLS - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True

        return False

# @leet end
