class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(treeA, treeB):
            if not treeA and not treeB:
                return True

            if not treeA or not treeB:
                return False
            
            if treeA.val != treeB.val:
                return False

            return isSameTree(treeA.left, treeB.left) and isSameTree(treeA.right, treeB.right)

        if not root:
            return False


        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)