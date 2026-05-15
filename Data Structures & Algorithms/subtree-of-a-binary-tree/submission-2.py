class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.isSametree(root,subRoot):
            return True 

        return (self.isSubtree(root.right,subRoot) or 
                self.isSubtree(root.left,subRoot)) 
        

    def isSametree(self, s, t):
        if not s and not t :
            return True 
        if s and t and s.val == t.val:
            return (self.isSametree(s.left,t.left) and
                    self.isSametree(s.right,t.right))
        return False