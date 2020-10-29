# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return

        visited = set()
        curr = head

        while curr is not None:

            if curr in visited:
                return curr

            visited.add(curr)
            curr = curr.next

        return