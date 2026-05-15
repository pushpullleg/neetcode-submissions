class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {},{}

        for i in s:
            count_s[i] = 1 + count_s.get(i, 0)
        
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        
        if count_s != count_t : return False
        
        for i in count_s:
            if count_s[i] != count_t[i]:
                return False

        return True
        