class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_elements_dict = {}
        temp_list = []
        return_list = []
        
        for i in nums:
            # creating dictionary with number as key and its frequency as value
            frequent_elements_dict[i] = 1 + frequent_elements_dict.get(i, 0)
        
        for key, val in frequent_elements_dict.items():
            # preparing a list of list holding frequency and the number itself
            temp_list.append([val, key]) 

        # Sorting the list so that highest frequency will be added at the end
        temp_list.sort()

        while len(return_list) < k:
            # popping the elements until the count of k
            return_list.append(temp_list.pop()[1])

        return return_list
