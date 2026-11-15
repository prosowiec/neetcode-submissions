class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxElement = max(piles)

        #elementRange = [i for i in range(maxElement + 1)]

        l, r = 0, maxElement

        k_res = maxElement
        while l <= r:
            k = l + (r - l) // 2
            
            if k <= 0:
                break
            
            rate  = 0
            for e in piles:
                rate += -(-e // k)


            if rate <= h:
                k_res = min(k_res, k)
                r = k - 1
            if rate > h:
                l = k + 1
        
        return k_res