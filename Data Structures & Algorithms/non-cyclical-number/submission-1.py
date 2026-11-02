class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit*digit
                n = n // 10
            if sum in seen:
                return False
            
            if sum == 1:
                return True

            seen.add(sum)
            n = sum
