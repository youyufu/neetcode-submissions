class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i_start = 0
        i_end = len(matrix) - 1
        j_start = 0
        j_end = len(matrix[0]) - 1
        while i_start <= i_end and j_start <= j_end:
            mid_i = (i_start + i_end) // 2
            mid_j = (j_start + j_end) // 2
            if matrix[mid_i][mid_j] == target:
                return True
            elif matrix[mid_i][mid_j] > target:
                if matrix[mid_i][0] > target:
                    i_end = mid_i - 1
                else:
                    j_end = mid_j - 1
            else:
                if matrix[mid_i][-1] < target:
                    i_start = mid_i + 1
                else:
                    j_start = mid_j + 1
        return False
