# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        return self._reverse(head)
    def _reverse(self, node, prev = None):
        if not node:    return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
        
        
        # prev = None
        # while head:
        #     curr = head
        #     head = head.next
        #     curr.next = prev
        #     prev = curr
        # return prev
        
        # cur, prev = head, None
        # while cur:
        #     cur.next, prev, cur = prev, cur, cur.next
        # return prev
        
        # i = []
        # s1 = head
        # s2 = head
        # while s1 != None:
        #     i.append(s1.val)
        #     s1 = s1.next
        # count = len(i)-1
        # while s2 != None:
        #     s2.val = i[count]
        #     count -= 1
        #     s2 = s2.next
        # return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        