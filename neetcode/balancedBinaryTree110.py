# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def depth(node):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            return 1 + max(left, right)

        if abs(depth(root.left) - depth(root.right)) > 1:
            return False
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
    
        return True
