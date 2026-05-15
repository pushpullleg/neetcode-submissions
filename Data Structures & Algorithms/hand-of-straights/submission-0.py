class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = {}
        for i in hand:
            count[i] = 1 + count.get(i, 0)
        minHeap = list(count)
        heapq.heapify(minHeap)
        while minHeap:
            top = minHeap[0]
            for i in range(top, top + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    heapq.heappop(minHeap)
        return True
        