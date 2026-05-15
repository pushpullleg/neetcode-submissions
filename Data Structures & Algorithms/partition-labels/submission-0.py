class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i, c in enumerate(s):
            lastIdx[c] = i
        print(lastIdx)
        size = 1
        res = []
        end = lastIdx[s[0]]
        for i, c in enumerate(s):
            end = max(lastIdx[c], end)
            if i == end:
               res.append(size) 
               size = 0
            size += 1
        return res
        