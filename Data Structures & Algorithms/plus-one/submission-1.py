class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        print(digits)
        n = 0
        carry = 1
        while n < len(digits):
            if digits[n] == 9 and carry:
                digits[n] = 0
                carry = 1
            else:
                digits[n] += carry
                carry = 0
            n += 1
        if carry: digits.append(carry)
        return digits[::-1]
        