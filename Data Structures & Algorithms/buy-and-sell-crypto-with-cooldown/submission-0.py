class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} #key:(i, buy/sell) val: maximum profit at i
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            cooldown = dfs(i + 1, buy)
            if buy:
                dp[(i, buy)] = max(cooldown, dfs(i + 1, not buy) - prices[i])
            else:
                dp[(i, buy)] = max(cooldown, dfs(i + 2, not buy) + prices[i])
            return dp[(i, buy)]
        return dfs(0, True)