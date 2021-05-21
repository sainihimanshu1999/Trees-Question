'''
In this question we have to find the minimum difference between any two different nodes in the tree
'''

def minDiff(self,root):
    self.result = float('inf')
    self.pre = float('-inf')

    def dfs(node):
        if node.left:
            dfs(node.left)

        self.result = min(self.result, abs(node.val-self.pre))
        self.pre = node.val

        if node.right:
            dfs(node.right)

    return self.result