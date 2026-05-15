class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            newdp = dp.copy()
            for t in newdp:
                if t + nums[i] == target:
                    return True
                dp.add(t + nums[i])
        return False