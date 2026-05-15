class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minval = nums[l]
        while nums[r] < nums[l]:
            minval = nums[r]
            r -= 1
        return minval

        