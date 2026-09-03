class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        l = 0
        r = num_rows*num_cols -1
        
        while l<=r:
            m = (l+r)//2

            row = m // num_cols
            col = m % num_cols

            value = matrix[row][col]

            if value == target:
                return True
            elif value>target:
                r=m-1
            else:
                l=m+1
        return False
