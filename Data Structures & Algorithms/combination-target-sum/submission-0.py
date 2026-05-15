class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, temp, tot_sum):
            if tot_sum == target:
                res.append(temp.copy())
                return
            if i >= len(nums) or tot_sum > target:
                return
                
            temp.append(nums[i])
            dfs(i, temp, tot_sum + nums[i])
            temp.pop()
            dfs(i + 1, temp, tot_sum)
        dfs(0, [], 0)
        return res