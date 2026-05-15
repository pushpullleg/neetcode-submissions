class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        def validate_palindrome(l, r):
            nonlocal res, res_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l: r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1
        for i in range(len(s)):
            l, r = i, i # odd length
            validate_palindrome(l, r)
            l , r = i, i + 1 # even length
            validate_palindrome(l, r)
        return res

