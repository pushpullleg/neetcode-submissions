class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        #[ flower, flow, fowl]
        # so looping thru 1st index i.e, "flower" which is len of 6
        for i in range(len(strs[0])):
            for s in strs:
                """
                checking if 1st index's 1st value is present in each element
                f is present in flower, flow and fowl
                2nd interation: checking if l is present in each elemetn
                l is present in flow but not in fowl
                so it will return the characters before i, i.e, 2.
                so the returned string will be just "f"
                """
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]