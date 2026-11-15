class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        pointOfRotation = l + (r-l)//2
        minElement = float('inf') 
        while l<=r:
            rightCheck = min(pointOfRotation + 1, r)
            leftCheck = max(pointOfRotation - 1, l)
            if nums[pointOfRotation] < nums[r]:
                r = pointOfRotation
            else:
                l = pointOfRotation + 1

            minElement = min(nums[pointOfRotation], minElement)
            pointOfRotation = l + (r-l) // 2
        

        return int(minElement)
