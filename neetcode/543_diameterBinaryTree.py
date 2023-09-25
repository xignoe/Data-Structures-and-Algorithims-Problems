class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def depth(node):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # Update the diameter by taking the sum of the longest paths in the left and right subtrees
            diameter[0] = max(diameter[0], left + right)
            return 1 + max(left, right)

        depth(root) # Calculate the depths and update the diameter
        return diameter[0]
