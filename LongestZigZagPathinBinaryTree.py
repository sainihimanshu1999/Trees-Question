'''
Longest Zig Zag Path in Binary tree
'''
def zigZag(self,root):
    def dfs(node,l,r):
        if node:
            res[0] = max(res[0],l,r)
            dfs(node.left,0,l+1)
            dfs(node.right,r+1,0)
    res = [0]
    dfs(root,0,0)
    return res[0]
