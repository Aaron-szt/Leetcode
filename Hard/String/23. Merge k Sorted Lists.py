# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next



import collections
class Solution:
    def mergeKLists(self, lists):
        
        
        def quick_sort(td, L, R):
            l = L
            r = R
            if l < r:
                key = td[l]
                while l != r:
                    while l < r and td[r][0] >= key[0]:
                        r -= 1
                    td[l] = td[r]

                    while l < r and td[l][0] <= key[0]:
                        l += 1
                    td[r] = td[l]
                    
                td[l] = key
                td = quick_sort(td, L, l - 1)
                td = quick_sort(td, r + 1, R)
            return td
        
        
        def insert_sort(td):
            if len(td) == 1:
                return td
            if len(td) > 1 and td[0][0] <= td[1][0]:
                return td
            tmp = td.pop(0)
            new = []
            for t in range(len(td) - 1):
                if td[t][0] < tmp[0] and td[t + 1][0] >= tmp[0]:
                    new = td[0 : t + 1]
                    new.append(tmp)
                    new += td[t + 1:]
            if len(td) > 0 and td[len(td) - 1][0] <= tmp[0] and new == []:
                new = td[0:len(td)]
                new.append(tmp)
            return new
        
        
        def find_min(start, dic):
            min_index = dic[0][1]
            start.next = ListNode(lists[min_index].val)
            start = start.next
            if lists[min_index]:
                lists[min_index] = lists[min_index].next
                if lists[min_index]:
                    dic[0][0] = lists[min_index].val
                else:
                    dic.pop(0)
            return start, dic
        
        start = ListNode(0)
        ans = start
        dic = [[-1, -1] for _ in lists]
        for i, l in enumerate(lists):
            if l:
                dic[i][0] = l.val
                dic[i][1] = i
        while [-1,-1] in dic:
            dic.remove([-1,-1])

        l = 0
        r = len(dic) - 1
        dic = quick_sort(dic, l, r)
        
        while dic:
            dic = insert_sort(dic)
            if dic:
                start, dic = find_min(start, dic)
            
        
        return ans.next
        
        
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        