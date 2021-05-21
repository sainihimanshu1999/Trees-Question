'''
here we are given two trees we have to find wheter the sequence to leaf nodes are saem in both the trees
'''

def similarLeaf(self,root1,root2):
    def dfs(node):
        if not node: return None
        if not node.left and not node.right: return [node.val]
        return dfs(node.left)+dfs(node.right)