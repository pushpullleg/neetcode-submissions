class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            curr = nums[i]
            remaining = target - curr
            if remaining in hashMap:
                return [hashMap[remaining], i]
            hashMap[curr] = i