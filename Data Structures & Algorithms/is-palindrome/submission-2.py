class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ptr1 = 0
        ptr2 = len(s) - 1
        for i in range(len(s)):
            if not s[ptr1].isalnum():
                ptr1 += 1
                continue
            if not s[ptr2].isalnum():
                ptr2 -= 1
                continue
            if s[ptr1] != s[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1
        return True