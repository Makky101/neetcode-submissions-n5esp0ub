# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast is not None:
            if fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            else:
                break
            if slow is fast:
                return True
        return False

