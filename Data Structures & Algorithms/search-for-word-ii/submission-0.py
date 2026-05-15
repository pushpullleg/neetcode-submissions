class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

    def addwords(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isend = True

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        visited, res = set(), set()
        root = TrieNode()

        for word in words:
            root.addwords(word)

        def dfs(r, c, node, word):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or board[r][c] not in node.children:
                return
            visited.add((r,c))
            word += board[r][c]

            node = node.children[board[r][c]]

            if node.isend:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)