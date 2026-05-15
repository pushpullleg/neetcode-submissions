class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, summed):
            if summed == target and cur.copy() not in res:
                res.append(cur.copy())
                return
            if i >= len(candidates) or summed > target:
                return
            cur.append(candidates[i])
            dfs(i + 1, cur, summed + candidates[i])
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, summed)
        dfs(0, [], 0)
        return res