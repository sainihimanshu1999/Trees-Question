'''
In this question we have to find the longest path which does not need to necessarily include route
'''

def diamete(self,root):
    self.result = 0
    def dfs(node):
        if not node: return 0

        ldepth = dfs(node.left)
        rdepth = dfs(node.right)

        self.result = max(self.result, ldepth+rdepth)

        return 1+max(ldepth+rdepth)

    dfs(root)
    return self.result

