def findBottomValue(self,root):
    q = [root]
    ans = 0
    while q:
        ans = q[0].val

        for i in range(len(q)):
            node = q.pop(0)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

    return ans