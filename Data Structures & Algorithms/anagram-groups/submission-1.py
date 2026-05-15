class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_str = {}
        for curr_str in strs:
            sorted_curr_str = tuple(sorted(curr_str))
            if sorted_curr_str in dict_str:
                dict_str[sorted_curr_str].append(curr_str)
            else:
                dict_str[sorted_curr_str] = [curr_str]
        return list(dict_str.values())