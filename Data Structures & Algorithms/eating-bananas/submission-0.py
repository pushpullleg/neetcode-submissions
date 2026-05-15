class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum rate at which koko could eat banana is 1 and max would be the max of pile
        l, r = 1, max(piles)
        res = r

        while l <= r:
            # finding the mid rate to see if the time is <= expected hours
            k = (l + r) // 2
            total_time = 0
            for i in piles:
                total_time += math.ceil(i / k)

            if total_time <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
