class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        # 1 way of making up the amount of 0 with a single coin - by using no coin
        for i in range(n):
            dp[i][0] = 1 # base case of resetting 1st column of amount 0 to 1
        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a] + dp[i][a - coins[i]]
        return dp[0][amount]