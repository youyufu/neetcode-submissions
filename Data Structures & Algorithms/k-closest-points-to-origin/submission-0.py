class NodeWrapper:
    def __init__(self, x, y):
        self.coords = [x, y]
        self.dist = math.sqrt(x**2 + y**2)
    
    def __lt__(self, other):
        return self.dist < other.dist

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for xi, yi in points:
            heapq.heappush(heap, NodeWrapper(xi, yi))
        res = []
        for i in range(k):
            node = heapq.heappop(heap)
            res.append(node.coords)
        return res