class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary Search on Rows
        topRow = 0
        botRow = len(matrix)-1
        mRow = 0
        while (botRow >= topRow):
            mRow = (topRow + botRow) //2
            if (matrix[mRow][-1] < target):
                topRow = mRow +1
            elif (matrix[mRow][0] > target):
                botRow = mRow -1
            else:
                break

        if (not(topRow <= botRow)):
            return False

        #Binary Search on Row M
        l = 0
        r = len(matrix[0]) -1
        while (l <= r):
            m = (l + r) // 2
            if (matrix[mRow][m] < target):
                l = m +1
            elif (matrix[mRow][m] > target):
                r = m -1
            else:
                return True

        return False