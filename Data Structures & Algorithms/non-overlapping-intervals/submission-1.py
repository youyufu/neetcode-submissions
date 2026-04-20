class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start times
        intervals.sort(key=lambda i: i[0])
        # greedy interval removal
        prevend = intervals[0][1]
        num_rm = 0
        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end
            else:
                num_rm += 1
                prevend = min(end, prevend)
        return num_rm