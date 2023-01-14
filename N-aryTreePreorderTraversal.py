class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root: return []
        
        nodes = [root.val]
        
        for node in root.children:
            
            nodes.extend(self.preorder(node))
        
        return nodes
