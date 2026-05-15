class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charset = set()
        maxi = 0

        for r in range(len(s)):  #mistake index 
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            maxi = max( maxi, r - l + 1)

        return maxi




        