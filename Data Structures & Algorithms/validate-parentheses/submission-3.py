class Solution:
    def isValid(self, s: str) -> bool:
        dict = { ')' : '(', '}' : '{', ']' : '[' }
        stack = []
        for c in s:
            if c in dict:
                if stack and stack[-1] == dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0