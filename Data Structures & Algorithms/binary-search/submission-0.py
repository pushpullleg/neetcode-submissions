class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[j] == target:
                return j
            j -= 1
        return -1