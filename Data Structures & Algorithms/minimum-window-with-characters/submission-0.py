class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # convert s, t to hash
        t_hash = {}
        for ch in t:
            t_hash[ch] = 1 + t_hash.get(ch, 0)

        s_hash = {}
        have, need = 0, len(t_hash)
        res = [-1, -1]
        reslen = float("inf")
        l = 0
        for r in range(len(s)):
            ch = s[r]
            s_hash[ch] = 1 + s_hash.get(ch, 0)
            if ch in t_hash and t_hash[ch] == s_hash[ch]:
                have += 1
            
            while have == need:
                if r - l + 1 < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                
                s_hash[s[l]] -= 1
                if s[l] in t_hash and s_hash[s[l]] < t_hash[s[l]]:
                    have -=1
                l += 1
        return s[res[0]: res[1]+1] if reslen != float("inf") else ""
