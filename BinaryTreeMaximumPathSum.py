'''
In this question we have to find the maximum path sum in the binary tree, it does not need to include root
'''

def maximumPath(self,root):
    self.maxPath = 0
    def dfs(node):
        if not node: return 0

        left = max(dfs(node.left),0)
        right = max(dfs(node.right),0)

        currentPath = node.val + left + right
        self.maxPath = max(self.maxPath,currentPath)

        return node.val + max(left,right)

    dfs(root)
    return self.maxPath