class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        def findp(n):
            while n != parent[n]: # continues until a root node(self-parent)
                parent[n] = parent[parent[n]] # path-halving: skip one level
                n = parent[n]
            return n

        def union(u, v):
            p1 = findp(u)
            p2 = findp(v)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]