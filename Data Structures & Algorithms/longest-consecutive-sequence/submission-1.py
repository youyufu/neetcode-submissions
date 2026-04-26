class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}  # seen[num] = [end_len, start_len]
        longest = 0

        for num in nums:
            if num in seen:
                continue

            left  = seen[num - 1][0] if num - 1 in seen else 0  # seq length ending at num-1
            right = seen[num + 1][1] if num + 1 in seen else 0  # seq length starting at num+1
            total = left + 1 + right

            seen[num] = [left + 1, right + 1]  # num itself is a boundary on both sides

            # Only the outer boundaries matter for future lookups
            if left:
                seen[num - left][1] = total   # update start_len at left boundary
            if right:
                seen[num + right][0] = total  # update end_len at right boundary

            longest = max(longest, total)

        return longest