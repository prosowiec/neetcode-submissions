class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productOfAll = 1
        zeroCount = 0
        for e in nums:
            if e != 0:
                productOfAll = productOfAll * e
            else:
                zeroCount += 1

        if zeroCount > 1:
            return [0] * len(nums)

        res = []
        for e in nums:
            if zeroCount == 1 and e != 0:
                res.append(0)
            elif e == 0:
                res.append(productOfAll)
            else:
                res.append(productOfAll // e)

        return res