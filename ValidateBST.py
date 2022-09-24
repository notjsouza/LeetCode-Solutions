
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def iter(root, minNode, maxNode) -> bool:
            
            if not root: return True
            if minNode and root.val <= minNode.val: return False
            if maxNode and root.val >= maxNode.val: return False
            
            return iter(root.right, root, maxNode) and iter(root.left, minNode, root)
        
        return iter(root, None, None)
