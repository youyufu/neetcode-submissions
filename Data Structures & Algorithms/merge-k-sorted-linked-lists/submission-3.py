# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrap:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # make min heap with value of each head
        minheap = []
        for linklist in lists:
            if linklist:
                heapq.heappush(minheap, NodeWrap(linklist))
        res = ListNode(0)
        curr = res

        while minheap:
            node_wrapper = heapq.heappop(minheap)
            node = node_wrapper.node
            if node.next:
                heapq.heappush(minheap, NodeWrap(node.next))
            curr.next = ListNode(node.val)
            curr = curr.next

        return res.next