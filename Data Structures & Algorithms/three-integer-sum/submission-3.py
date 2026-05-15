class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
                if a > 0:
                    break 
                if i != 0 and a == nums[i - 1]:
                    continue #keep the 1st element untouched
                             #current element is not the same as previous element
                
                l, r = i + 1, len(nums) - 1
                while l < r:
                
                    sums = nums[l] + nums [r] + a  

                    if sums > 0:
                        r -= 1
                    elif sums < 0:
                        l += 1
                    else:
                        res.append([nums[l], a, nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1] :
                            l += 1

        return res
                
                
        