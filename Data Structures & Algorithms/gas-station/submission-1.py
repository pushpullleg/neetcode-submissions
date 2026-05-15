class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        rem = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            rem += (gas[i] - cost[i])
            if rem < 0:
                start = i + 1
                rem = 0
            #print(rem)
        return start