class Solution(object):
    def lengthOfLastWord(self, s):
        index=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                pass
            elif s[i]!=' ' and i-1>=0:
                if s[i-1]==' ':
                    index+=1
                    return index
                else:
                    index+=1
            else:
                index+=1
 
        return index
            


        
