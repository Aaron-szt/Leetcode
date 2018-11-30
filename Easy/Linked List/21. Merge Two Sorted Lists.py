class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:  return l2
        if not l2:  return l1
        
        start = ListNode(0)
        ans = start
        
        while l1 and l2:
            if l1.val < l2.val:
                start.next = ListNode(l1.val)
                l1 = l1.next
                start = start.next
            else:
                start.next = ListNode(l2.val)
                l2 = l2.next
                start = start.next
        
        while l1:
            start.next = ListNode(l1.val)
            l1 = l1.next
            start = start.next
        while l2:
            start.next = ListNode(l2.val)
            l2 = l2.next
            start = start.next
        
        return ans.next