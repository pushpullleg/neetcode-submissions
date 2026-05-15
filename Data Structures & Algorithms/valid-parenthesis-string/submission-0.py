class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin = leftmax = 0
        for c in s:
            if c == "(":
                leftmin, leftmax = leftmin + 1, leftmax + 1
            elif c == ")":
                leftmin, leftmax = leftmin - 1, leftmax - 1
            else:
                leftmin = leftmin - 1 # when ) is considered
                leftmax = leftmax + 1 # when ( is considered
            if leftmin < 0:
                leftmin = 0
            if leftmax < 0: # no choices left to make it valid in the best case
                return False
            print(leftmin, leftmax)
        return leftmin == 0