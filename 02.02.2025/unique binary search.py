
class Solution(object):
    def generateTrees(self, n):
    
        def gen(l,n):
            if n<l:
                return [None]
            if l==n:
                t = TreeNode(n)
                return [t]

            trees = []
            for root in range(l,n+1):
              left_child_options= gen(l,root-1)
              right_child_options = gen(root+1, n)
              for left in left_child_options:
                for right in right_child_options:
                   t = TreeNode(root)
                   t.left= left
                   t.right = right
                   trees.append(t)
            return trees
        return gen(1,n)        
