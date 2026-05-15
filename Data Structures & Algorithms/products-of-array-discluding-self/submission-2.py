class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        size = len(nums)
        res = [1] * size
        print("Prefix:")
        for i in range(size):
            res[i] = prefix
            prefix *= nums[i]
            print(res[i])
        print("Postfix:")
        for i in range(size-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
            print(res[i])
        return res
