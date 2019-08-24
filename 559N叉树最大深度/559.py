class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
            if root.children==None:
                return 1

        return  1 + max(map(self.maxDepth, root.children))
