class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        numset = set(nums)
        length, longest = 1, 1
        for num in numset:
            if num - 1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1
                longest = max(length, longest)

        return longest