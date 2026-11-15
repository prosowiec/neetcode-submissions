class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kLargest = k        
        self.currNums = sorted(nums)
        self.curKLargest = k

    def add(self, val: int) -> int:
        l,r=0,len(self.currNums)-1

        while l<=r:
            mid = l + (r-l)//2

            if self.currNums[mid] == val:
                l = mid
                break
            if val > self.currNums[mid]:
                l=mid+1
            else:
                r=mid-1
                
        self.currNums.insert(l, val)

        return self.currNums[-self.kLargest]