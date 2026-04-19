class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time: nlog n
        intervals.sort()
        # loop over intervals: merge until not overlapping with next for each - n
        i = 0
        while i < len(intervals):
            while i+1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            i += 1
        return intervals