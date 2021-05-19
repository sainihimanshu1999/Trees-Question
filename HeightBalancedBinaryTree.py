'''
In this question, we calculate depth at every height and then see if the tree is balanced
'''

def isBalanced(self,root):
    def dfs(self,node):
        if not node: return 0
        return 1+max(node.left,node.right)

    ldepth = dfs(root.left)
    rdepth = dfs(root.right)

    if abs(ldepth-rdepth)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
        return True