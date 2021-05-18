'''
In this question we will do simple bfs but keep a variable of direction and keep changing it one every
level
'''

def zigZag(self,root):
    if not root: return []

    q = [root]
    result =[]
    direction = 1

    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level[::direction])
        direction *= -1
    return result