def rightSide(self,root):
    def dfs(node,depth):
        if node:
            if depth == len(self.res):
                self.res.append(node.val)

            dfs(root.right,depth+1)
            dfs(root.left,depth+1)

    self.res = []    
    dfs(root,0)
    return self.res