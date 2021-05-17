'''
In this question we have to return an array which gives the nodes to be flipped to get make the current
tree equal to it's preorder traversal tree
'''

def flip(self,root,pre):
    res = []
    stack = [root]
    i=0

    while stack:
        node = stack.pop()
        if not node: continue

        if node and node.val != pre[i]: return [-1]

        i+=1

        if node.right and node.right.val == pre[i]:
            if node.left: res.append(node.val)
            stack.extend([node.left,node.right])
        else:
            stack.extend([node.right,node.left])

    return res