class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin, curmax = 1, 1
        res = nums[0]
        for i in nums:
            tempmin, tempmax = curmin, curmax
            curmin = min(i, tempmax * i, tempmin * i)
            curmax = max(i, tempmax * i, tempmin * i)
            res = max(res, curmax)
            #print(res)
        return res
        