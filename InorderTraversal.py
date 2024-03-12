class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = []
        if root.left:
            out += self.inorderTraversal(root.left)
        out.append(root.val)
        if root.right:
            out += self.inorderTraversal(root.right)
        return out
