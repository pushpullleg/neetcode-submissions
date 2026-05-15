class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
       adj = {c:set() for w in words for c in w}
       
       for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minlen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
                return ""
            else:
                for j in range(len(word1)):
                    if word1[j] != word2[j]:
                        adj[word1[j]].add(word2[j])
                        break
       print(adj)
       res = []
       visited = {}

       def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return ""
            visited[c] = False
            res.append(c)
       for c in adj:
            if dfs(c):
                return ""
       res.reverse()
       return "".join(res)