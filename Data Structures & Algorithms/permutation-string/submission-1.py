class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1, h2 = [0] * 26, [0] * 26
        matches = 0
        if len(s1) > len(s2): return False
        for i in range(len(s1)):
            h1[ord(s1[i]) - 97] += 1
            h2[ord(s2[i]) - 97] += 1
        
        for i in range(26):
            matches += 1 if h1[i] == h2[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            idxRight = ord(s2[r]) - 97
            h2[idxRight] += 1
            if h2[idxRight] == h1[idxRight]:
                matches += 1
            elif h2[idxRight] - 1 == h1[idxRight]:
                matches -= 1
            
            idxLeft = ord(s2[l]) - 97
            h2[idxLeft] -= 1
            if h2[idxLeft] == h1[idxLeft]:
                matches += 1
            elif h2[idxLeft] + 1 == h1[idxLeft]:
                matches -= 1
            
            l += 1
        
        return matches == 26
        