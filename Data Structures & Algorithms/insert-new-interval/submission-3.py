class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        j = len(intervals) - 1
        while i <= j:
            mid = (i+j)//2
            if intervals[mid][0] < newInterval[0]:
                i = mid + 1
            else:
                j = mid - 1
        intervals.insert(i, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res