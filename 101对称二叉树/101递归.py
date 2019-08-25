class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right) 
        def isMirror(self, p, q):  
            if not p or not q:
                return True
            if not p or not q:
                return False
            l= self.isMirror(p.left, q.right)           
            r = self.isMirror(p.right, q.left)
            return p.val=q.val and l and r


