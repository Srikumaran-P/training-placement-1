class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=bin(n)
        n=str(n)
        count=0
        for _ in n:
            if _=='1':
                count+=1
        return count
        
