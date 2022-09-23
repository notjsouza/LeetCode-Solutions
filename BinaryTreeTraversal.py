class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hashMap = {}
        
        def trav(root, level):
            
            if not root: return
            
            if level in hashMap: hashMap[level].append(root.val)
            else: hashMap[level] = [root.val]
            
            trav(root.left, level + 1)
            trav(root.right, level + 1)
            
        trav(root, 0)
        
        n = []
        for l, v in hashMap.items():
            n.append(v)
        
        return n
