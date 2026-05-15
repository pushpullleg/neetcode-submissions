class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minm = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                minm = min(minm, nums[l])
                break
            m = (l + r) // 2
            minm = min(minm, nums[m])
            if nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
        return minm

