'''
Minimum the difference in two different nodes in binary tree
'''

def minDiff(self,root):
    self.pre = float('-inf')
    self.result = float('inf')

    def dfs(node):
        if node.left:
            dfs(node.left)
        self.res = min(self.res,root.val-self.pre)
        self.pre = root.val

        if node.right:
            dfs(node.right)
        return self.res
    return dfs(root)