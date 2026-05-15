class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i, c in enumerate(s):
            lastIdx[c] = i
        print(lastIdx)
        size = end = 0
        res = []
        for i, c in enumerate(s):
            end = max(lastIdx[c], end)
            size += 1
            if i == end:
               res.append(size) 
               size = 0
        return res
        