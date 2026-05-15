class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_str = {}
        anagram_list = []
        for curr_str in strs:
            sorted_curr_str = tuple(sorted(curr_str))
            if sorted_curr_str in dict_str:
                dict_str[sorted_curr_str].append(curr_str)
            else:
                dict_str[sorted_curr_str] = [curr_str]

        for val in dict_str.values():
            anagram_list.append(val)
            print(val)

        return anagram_list