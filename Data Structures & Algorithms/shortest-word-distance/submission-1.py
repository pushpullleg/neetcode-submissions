class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1
        distance = len(wordsDict)
        for idx, word in enumerate(wordsDict):
            if word1 == word:
                i1 = idx
            if word2 == word:
                i2 = idx
            if i1 != -1 and i2 != -1:
                distance = min(distance, abs(i1-i2))
        return distance