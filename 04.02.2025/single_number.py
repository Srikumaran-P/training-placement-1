class Solution(object):
    def singleNumber(self, nums):
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for j in dict:
            if dict[j]==1:
                return j
                

       
        
