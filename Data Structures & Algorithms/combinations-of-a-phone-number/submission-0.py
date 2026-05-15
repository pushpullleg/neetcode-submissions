class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_alpha = {"2": "abc", "3":"def","4":"ghi", "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def backtrace(i, temp):
            if len(temp) == len(digits):
                res.append(temp)
                return
            for c in digit_alpha[digits[i]]:
                backtrace(i + 1, temp + c)
        if digits: 
            backtrace(0, "")

        return res