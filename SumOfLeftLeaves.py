'''
Sum of left leaves in tree
'''

def leftLeaves(self,root):
    def dfs(node,dr):
        if not node:return 

        if not node.left and not node.right:
            if dr == -1:
                self.result += node.val

        dfs(node.left,-1)
        dfs(node.right,1)

    self.result = 0
    dfs(root,0)
    return self.result
