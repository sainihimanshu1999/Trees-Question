def PathSum(self,root):
    self.result = []
    def dfs(node,path):
        if not node: return
        if not node.left and not node.right:
            path += str(node.val)
            self.result.append(path)

        dfs(node.left, path+str(node.val)+'->')
        dfs(node.right, path+str(node.val)+'->')

    dfs(root,'')
    return self.result
    