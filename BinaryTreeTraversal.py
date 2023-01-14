class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        d = {}
        
        def trav(root, level):
            
            if not root: return
            
            if level in d: d[level].append(root.val)
            else: d[level] = [root.val]
            
            trav(root.left, level + 1)
            trav(root.right, level + 1)
            
        trav(root, 0)
        
        n = []
        for l, v in d.items():
            n.append(v)
        
        return n
