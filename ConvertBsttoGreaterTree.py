'''
we convert BST to Greater Tree, Greater Tree means, every node will have node value = sum of all greater
nodes present in the tree including it's own value
'''

def convertBst(self,root):
    self.sumi = 0
    def dfs(node):
        if not node: return None
        dfs(node.right)
        self.sumi += node.val
        node.val = self.sumi
        dfs(node.left)
    return dfs(root)

