# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_strt = None
        merged = merged_strt
        curr1 = list1
        curr2 = list2
        while curr1 is not None or curr2 is not None:
            if curr1 is None:
                new_node = ListNode(val=curr2.val)
                if merged is None:
                    merged = new_node
                    merged_strt = merged
                else:
                    merged.next = new_node
                    merged = merged.next
                curr2 = curr2.next
            elif curr2 is None:
                new_node = ListNode(val=curr1.val)
                if merged is None:
                    merged = new_node
                    merged_strt = merged
                else:
                    merged.next = new_node
                    merged = merged.next
                curr1 = curr1.next
            else:
                if curr1.val < curr2.val:
                    new_node = ListNode(val=curr1.val)
                    if merged is None:
                        merged = new_node
                        merged_strt = merged
                    else:
                        merged.next = new_node
                        merged = merged.next
                    curr1 = curr1.next
                else:
                    new_node = ListNode(val=curr2.val)
                    if merged is None:
                        merged = new_node
                        merged_strt = merged
                    else:
                        merged.next = new_node
                        merged = merged.next
                    curr2 = curr2.next
        return merged_strt

        