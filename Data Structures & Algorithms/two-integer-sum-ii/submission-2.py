class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        list_to_set = set(numbers)
        for i in list_to_set:
            if target - i in list_to_set and i != target - i:
                index_1 = numbers.index(i) + 1
                index_2 = numbers.index(target - i) + 1
        return [min(index_1, index_2) , max(index_1, index_2) ]