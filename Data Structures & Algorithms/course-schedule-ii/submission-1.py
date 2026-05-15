class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {n:[] for n in range(numCourses)}
        for c, p in prerequisites:
            premap[c].append(p)
        print(premap)
        res, visited = [], set()
        def dfs(crs):
            if crs in visited:
                return False
            if premap[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            visited.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            res.append(crs)
            premap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        