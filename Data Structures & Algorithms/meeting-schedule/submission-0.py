"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
         # sort intervals by start time
        sorted_interval = sorted(intervals, key=lambda x: x.start)
        print(sorted_interval)
        for i in range(1, len(intervals)):
            if sorted_interval[i].start < sorted_interval[i - 1].end:
                return False
        return True
