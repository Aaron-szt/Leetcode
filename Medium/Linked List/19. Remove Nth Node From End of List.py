# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = ListNode(0)
        fast.next = head
        slow = fast
        ans = fast
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return ans.next
        
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        