class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def callback(opening, closing):
            if opening == closing == n:
                res.append("".join(stack))
                return
            if opening < n:
                stack.append("(")
                callback(opening + 1, closing)
                stack.pop()
            if closing < opening:
                stack.append(")")
                callback(opening , closing + 1)
                stack.pop()
        callback(0, 0)
        return res

        