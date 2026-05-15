class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graphmap = {i: [] for i in range(n)}
        for i, j in edges:
            graphmap[i].append(j)
            graphmap[j].append(i)
       # print(graphmap)
        visited = set()
        def dfs(n, prev):
            if n in visited:
                return False
            visited.add(n)
            for adj in graphmap[n]:
                if adj == prev:
                    continue
                if not dfs(adj, n):
                    return False
            return True
        return dfs(0, -1) and n == len(visited)