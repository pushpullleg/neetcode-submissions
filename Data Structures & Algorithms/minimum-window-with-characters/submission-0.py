class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        # setting the dictionary for string t with the count
        # if t is "abca" then dict looks like {a:2, b:1,c:1}
        dict_t = {}
        dict_window = {}
        for i in t:
            dict_t[i] = 1 + dict_t.get(i, 0)

        l = r = matches = 0
        need = len(dict_t) # store this to check if window lenght matches
        res = [-1, -1]
        reslen = float("infinity")
        for r in range(len(s)):
            index = s[r]
            dict_window[index] = 1 + dict_window.get(index, 0)

            if index in dict_t and dict_window[index] == dict_t[index]:
                matches += 1

            while need == matches:
                if r - l + 1 < reslen:
                    res = [l, r]
                    reslen = r - l + 1
#remove the element from l before advancing the l pointer
                dict_window[s[l]] -= 1
                
                if s[l] in dict_t and dict_window[s[l]] < dict_t[s[l]]:
                    matches -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if reslen != float("infinity") else ""