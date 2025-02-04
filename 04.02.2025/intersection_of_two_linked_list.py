
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        temp1=headA
        temp2=headB
        if temp1==0 or temp2==0:
            return 0
        while temp1!=temp2:
            temp1=temp1.next if temp1 else headB
            temp2=temp2.next if temp2 else headA
        return temp1

        
