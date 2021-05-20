def titlBinary(self,root):
    self.sum = 0
    def dfs(node):
        if not node: return 0

        self.sum += abs(dfs(node.left)-dfs(node.right))

        return self.sum+dfs(node.left)+dfs(node.right)

    dfs(root)
    return self.sum