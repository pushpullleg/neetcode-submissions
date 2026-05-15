class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordmap = defaultdict(list)
        # building {"dog":["*og","d*g","do*"]}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                wordmap[pattern].append(word)
        #print(wordmap)
        q = deque([beginWord]) # imp to enclose as a list
        visited = set(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in wordmap[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        return 0