'''
We just have to find the binary level order traversal
'''

def binaryOrderTraversal(self,root):
    if not root: return []
    res = []
    q = [root]
    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            level.append(node)

        res.append(level)

    return res