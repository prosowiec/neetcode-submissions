class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        
        midHeight = 0
        while up <= down:
            midHeight = up + (down - up) // 2
            if matrix[midHeight][0] <= target and matrix[midHeight][-1] >= target:
                break
            elif matrix[midHeight][0] < target:
                up = midHeight + 1
            else:
                down = midHeight - 1
        
        while l <= r:
            mid = l + (r-l) // 2
            if matrix[midHeight][mid] == target:
                return True
            elif matrix[midHeight][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        
        return False
