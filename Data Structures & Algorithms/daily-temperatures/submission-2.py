class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, a in enumerate (temperatures):
            while stack and stack[-1][0] < a:
                temp, ind = stack.pop()
                res[ind] = i - ind
            stack.append([a,i])
        return res