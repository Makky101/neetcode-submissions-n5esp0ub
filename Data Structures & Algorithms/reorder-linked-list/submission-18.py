# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        store = []
        ordered = []

        while head:
            store.append(head)
            head = head.next
        l, r = 0, len(store) - 1

        while l <= r:
            ordered.append(store[l])
            l += 1
            if l <= r:
                ordered.append(store[r])
                r -= 1
        i = 0
        while i != len(ordered) - 1:
            ordered[i].next = ordered[i + 1]
            i += 1
        ordered[i].next = None
