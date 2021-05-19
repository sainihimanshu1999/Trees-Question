'''
It is similar to binary traversal, just we have to go from leaf node to top
'''

def levelOrder(self,root):
    if not root: return []
    q  = [root]
    self.res = []

    while q:
        level = []
        for i in range(len(q)):
            node = node.pop(0)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            level.append(node.val)

        self.res.append(level)
    return self.res[::-1]