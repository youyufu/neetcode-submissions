class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_vol = 0
        while i <= j:
            curr_vol = (j - i) * min(heights[i], heights[j])
            if curr_vol > max_vol:
                max_vol = curr_vol
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_vol