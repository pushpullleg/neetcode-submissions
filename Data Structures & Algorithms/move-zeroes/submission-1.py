class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_list = []
        zero_count = 0
        for i in nums:
            if i != 0:
                new_list.append(i)
            else:
                zero_count += 1

        while zero_count > 0:
            new_list.append(0)
            zero_count -= 1

        nums [:] = new_list