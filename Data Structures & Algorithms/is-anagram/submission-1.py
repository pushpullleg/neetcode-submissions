class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def makeDictionary(word: str) -> dict:
            hash_set = {}
            for i in word:
                if i in hash_set:
                    hash_set[i] += 1
                else:
                    hash_set[i] = 0
            return hash_set
        
        s1 = makeDictionary(s)
        t1 = makeDictionary(t)

        return s1 == t1