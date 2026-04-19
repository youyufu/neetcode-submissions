class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min.append(val)
        else:
            self.stack.append(val)
            if self.min[-1] < val:
                self.min.append(self.min[-1])
            else:
                self.min.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
