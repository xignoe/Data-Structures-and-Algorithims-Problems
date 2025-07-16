# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(root):
            def inorder(node):
                if node is not None:
                    inorder(node.left)
                    result.append(node.val)
                    inorder(node.right)
            
            result = []
            inorder(root)
            return result
        print(inorder_traversal(root))
        arr = inorder_traversal(root)
        return arr[k - 1]
        