class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minval = nums[l]
        while l <= r:
        # if the very first comparision itself passes
        # then no need of running checks, hence break
            if nums[l] < nums[r]:
                minval = min(minval, nums[l])
                break
            m = (l + r) // 2
            minval = min(minval, nums[m])
            if nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
        return minval

        