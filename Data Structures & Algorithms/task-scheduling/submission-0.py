class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [freq for freq in count.values()]
        heapq.heapify_max(maxHeap) # max heap of task frequencies

        time = 0
        q = deque() # [freq, availableTime]
        while maxHeap or q:
            time += 1
            if not maxHeap: # skip to next cooldown finish time
                time = q[0][1]
            else:
                freqLeft = heapq.heappop_max(maxHeap) - 1 # schedule most frequent
                if freqLeft > 0:
                    q.append([freqLeft, time + n]) # move to cooldown queue
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0]) # finished cooldown - move to max heap
        return time