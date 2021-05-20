'''
Good leaf pairs means distance of one leaf two other leaf if less than or equal to the distance given
'''

def goodLeaf(self,root,distance):
    self.count = 0
    def dfs(node):
        if not node: return []

        if not node.left and not node.right: return [1]

        left = dfs(node.left)
        right = dfs(node.right)

        self.count += sum(l+r<=distance for l in left for r in right)
        return [n+1 for n in left+right if n+1<distance]
    dfs(root)
    return self.count
    