class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            # part1 where num is included
            subset.append(nums[i])
            backtrack(i + 1, subset)
            # part2 where num is not included
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res
