class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j != i :
                    prod *= nums[j]
            lst.append(prod)
        return lst

        