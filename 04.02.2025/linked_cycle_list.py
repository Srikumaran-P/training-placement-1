# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        if(head == None):
            return False
        else:
            p = head
            while(p != None):
                if(p in s):
                    return True
                elif(p not in s):
                    s.add(p)
                    p = p.next
            return False
        
