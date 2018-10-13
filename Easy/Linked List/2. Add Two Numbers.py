# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        ans = ListNode(0)
        final = ans
        addition = 0
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                ans.val = l1.val + l2.val + addition
                l1 = l1.next
                l2 = l2.next
            elif l1 != None:
                ans.val = l1.val + addition
                l1 = l1.next
            elif l2 != None:
                ans.val = l2.val + addition
                l2 = l2.next
            
            if ans.val >= 10:
                addition = 1
                ans.val %= 10
            else:
                addition = 0
            
            if l1 != None or l2 != None:
                ans.next = ListNode(0)
                ans = ans.next
        
        
        if addition == 1:
            ans.next = ListNode(1)

        return final
            
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """