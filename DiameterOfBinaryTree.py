# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        def findDepth(n: Optional[TreeNode]) -> int:
            if not n:
                return 0
            return max(findDepth(n.left)+1, findDepth(n.right)+1)

        return max(findDepth(root.left) + findDepth(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
