class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        if len(self.left) == 0: # empty list so far
            self.left.append(num)
        elif len(self.right) == 0: # 1 element so far
            if num > self.left[0]:
                self.right.append(num)
            else:
                self.right.append(self.left[0])
                self.left[0] = num
        else:
            heapq.heappush_max(self.left, num) if num <= self.left[0] else heapq.heappush(self.right, num)
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, heapq.heappop_max(self.left))
        elif len(self.right) > len(self.left) + 1:
            heapq.heappush_max(self.left, heapq.heappop(self.right))

    def findMedian(self) -> float:
        n = len(self.left) + len(self.right)
        if n % 2 == 1:
            if len(self.left) > len(self.right):
                return self.left[0]
            else:
                return self.right[0]
        else:
            return (self.left[0]+self.right[0])/2
        