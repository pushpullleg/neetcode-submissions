class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for i in tokens:
            if i in operators:
                if i == '+':
                    val = stack[-2] + stack[-1]
                elif i == '-':
                    val = stack[-2] - stack[-1]
                elif i == '*':
                    val = stack[-2] * stack[-1]
                else:
                    val = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)
            else:
                stack.append(int(i))
        val = int(stack.pop())
        return val