class Trienode:
    def __init__(self):
        self.children = {}
        self.mark_end = False

class WordDictionary:

    def __init__(self):
        self.root = Trienode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()
            cur = cur.children[c]
        cur.mark_end = True
    
    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur = node

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False   
                elif c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.mark_end

        return dfs(0, self.root)
