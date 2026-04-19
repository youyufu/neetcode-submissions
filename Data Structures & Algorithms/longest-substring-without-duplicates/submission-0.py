class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currchar = set()
        l = 0
        maxlen = 0
        for r in range(len(s)):
            while s[r] in currchar:
                currchar.remove(s[l])
                l += 1
            currchar.add(s[r])
            if r - l + 1 > maxlen:
                maxlen = r - l + 1
        return maxlen