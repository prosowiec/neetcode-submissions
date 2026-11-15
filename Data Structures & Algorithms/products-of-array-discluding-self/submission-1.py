class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productOfAll = 1
        zeroCount = 0
        for e in nums:
            if e != 0:
                productOfAll = productOfAll * e
            else:
                zeroCount += 1
        print(zeroCount)
        res = []#[0] * len(nums)
        for i, e in enumerate(nums):
            if zeroCount > 0 and e != 0:
                res.append(0)
            elif e == 0 and zeroCount == 1:
                res.append(productOfAll)
            else:
                element = 0 if e == 0 else productOfAll // e
                res.append(element)

        return res