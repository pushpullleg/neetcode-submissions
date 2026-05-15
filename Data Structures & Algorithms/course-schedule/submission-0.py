class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for j, k in prerequisites:
            premap[j].append(k)
        visited = set()
        def dfs(cur):
            if cur in visited:
                return False
            if premap[cur] == []:
                return True
            visited.add(cur)
            for p in premap[cur]:
                if not dfs(p):
                    return False
            visited.remove(cur)
            premap[cur] = [] # for efficiency
            return True
            
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True