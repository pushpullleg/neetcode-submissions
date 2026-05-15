class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningsum = 0
        maxsum = nums[0]
        for n in nums:
            if runningsum < 0:
                runningsum = 0
            runningsum += n
            maxsum = max(maxsum, runningsum)
        return maxsum
        