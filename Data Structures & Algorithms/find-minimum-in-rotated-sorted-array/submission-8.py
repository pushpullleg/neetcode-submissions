class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mins = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                mins = min(mins,nums[l])
                break
        
            m = (l + r) // 2
            mins = min(mins, nums[m])
            if nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
        return mins