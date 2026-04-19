# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        reversed_list = ListNode(head.val)
        while head.next is not None:
            head = head.next
            new_node = ListNode(head.val)
            new_node.next = reversed_list
            reversed_list = new_node
        return reversed_list