class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #nums = sorted(nums)
        #print(nums)
        ##h_dict = {}
        for i, e in enumerate(nums):
            h_dict = {}
            l,r = 0, i +1
            while l< i:
                h_dict[e + nums[l]] = nums[l]
                l+=1

            while r<len(nums):
                if -nums[r] in h_dict.keys():
                    h_ = sorted([h_dict[-nums[r]], e, nums[r]])
                    if h_ not in res:
                        res.append(h_)
                    
                r+=1
                
                
        return res