class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        best_len = 0
        max_freq = 0
        for r in range(len(s)):
            freq[s[r]] = freq[s[r]] + 1 if s[r] in freq else 1
            max_freq = max(max_freq, freq[s[r]])
            while r + 1 - l - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            best_len = max(best_len, r + 1 - l)
        return best_len
