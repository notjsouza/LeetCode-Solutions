class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root: return []
        
        nodes = [root.val]
        
        for n in root.children:
            
            nodes.extend(self.preorder(n))
        
        return nodes
