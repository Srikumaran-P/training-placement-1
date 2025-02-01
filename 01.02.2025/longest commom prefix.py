class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        mini = len(min(strs,key=len))
        s=""
        
        for j in range(0,mini):
            temp = [[] for _ in range(0,len(strs))]
            for i in range(0,len(strs)):  
                temp[i].append(strs[i][j])
            temp2 = [item for k in temp for item in k]
            if ( len(set(temp2)) == 1 ):       
                s+=temp[i][0]
            else:
                break
            
        return s
        
