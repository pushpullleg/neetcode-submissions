class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        res = ""
        for i in range(min(len1, len2)):
            res += word1[i] + word2[i]
        if len1 > len2:
            res += word1[len2:]
        else:
            res += word2[len1:]
        print(res)
        return res
        