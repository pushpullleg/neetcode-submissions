class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dummy_dict = {}
        # using space complexity of O(n)
        for i in nums:
            dummy_dict[i] = dummy_dict.get(i, 0) + 1
            if dummy_dict[i] > 1:
                return i

        