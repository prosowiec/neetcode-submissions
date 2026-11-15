class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        maxConsecutive = 0
        for e in nums:
            if e - 1 not in numSet:
                lenght = 1
                while e + lenght in numSet:
                    lenght += 1
                maxConsecutive = max(maxConsecutive, lenght)
                    

        return maxConsecutive