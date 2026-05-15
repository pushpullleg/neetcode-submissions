class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #index, value pairs
        for index, value in enumerate(temperatures):
            # pop whenever incoming value is greater than top element
            while stack and value > stack[-1][1]:
                stackInd, StackTemp = stack.pop()
                res[stackInd] = index - stackInd
            stack.append((index, value))
        return res