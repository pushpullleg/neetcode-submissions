class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)
            elif char == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif char == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
            #print(stack)
        return len(stack) == 0
        