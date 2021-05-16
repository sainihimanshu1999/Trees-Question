'''
In this question we find maximum width of binary tree using, BFS technoque, we maintain a queue with
level and index of the most left element in the level and then subtract it from most right element's index
in the tree and update the answer at each level
'''

def maxWidth(self,root):
    if not root: return 0

    ret = 0
    q = [(root,0)]

    while q:
        ret = max(ret, q[-1][1] - q[0][1] +1)
        temp = []
        for node,i in q:
            if node.left: temp.append((node.left,2*i))
            if node.right: temp.append((node.right,2*i + 1))
        q = temp
    return ret