class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newintervals = [intervals[0]]
        print(newintervals)
        for start, end in intervals:
            previousEnd = newintervals[-1][1]
            if start <= previousEnd:
                newintervals[-1][1] = max(previousEnd, end)
            else:
                newintervals.append([start, end])

        return newintervals