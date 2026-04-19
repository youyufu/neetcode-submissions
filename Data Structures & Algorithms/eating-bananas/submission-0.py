class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            h_mid = 0
            for bananas in piles:
                h_mid += (bananas + mid - 1) // mid
            if h_mid > h:
                l = mid + 1
            else:
                r = mid - 1
        return l
