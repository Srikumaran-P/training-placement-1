class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        res = []
        for i in path:
            if i == "." or i == '':
                continue
            if i == "..":
                res = res[:len(res) - 1]
                continue
            res.append(i)
        return '/' + ('/').join(res)

            





    
        
