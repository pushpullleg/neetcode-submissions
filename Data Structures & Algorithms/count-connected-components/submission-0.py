class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()
        def dfs(node):
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
        res = 0
        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                res += 1
        return res

        