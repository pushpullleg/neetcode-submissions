# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def get_height(node: [TreeNode]) -> int:
        #without adding this, it would throw a exception saying
        # cannot access local variable
            nonlocal res
            if not node: return 0
            
            left = get_height(node.left)
            right = get_height(node.right)

            height = 1 + max(left, right)
            res = max(res, left + right)
            
            return height
        get_height(root)
        return res