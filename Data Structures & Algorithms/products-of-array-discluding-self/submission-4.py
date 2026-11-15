class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productOfAll = 1
        zeroCount = 0
        for e in nums:
            if e != 0:
                productOfAll = productOfAll * e
            else:
                zeroCount += 1

        res = [0] * len(nums)
        if zeroCount > 1:
            return res

        for i, e in enumerate(nums):
            if zeroCount == 1 and e != 0:
                res[i] = 0
            elif e == 0:
                res[i] = productOfAll
            else:
                res[i] = productOfAll // e

        return res