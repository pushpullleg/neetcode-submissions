class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range (len(tokens)):
            if tokens[i] == "+":
               e1 = stack.pop()
               e2 = stack.pop()
               stack.append(e1 + e2)
            elif tokens[i] == '-':
               e1 = stack.pop()
               e2 = stack.pop()
               stack.append(e2 - e1)
            elif tokens[i] == "*":
               e1 = stack.pop()
               e2 = stack.pop()
               stack.append(e1 * e2)
            elif tokens[i] == "/":
               e1 = stack.pop()
               e2 = stack.pop()
               stack.append(int(e2 / e1))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]