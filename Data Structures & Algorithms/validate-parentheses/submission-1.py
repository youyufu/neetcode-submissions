class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            if ch == ')':
                if not stack or stack.pop() != '(':
                    return False
            if ch == '}':
                if not stack or stack.pop() != '{':
                    return False
            if ch == ']':
                if not stack or stack.pop() != '[':
                    return False
        return not stack