'''
Similar to previous
'''

def LCA(self,root,p,q):
    if root == p and root == q:
        return root

    left = right = None
    if root.left:
        left = self.LCA(root.left,p,q)

    if root.right:
        right = self.LCA(root.right,p,q)

    if left and right:
        return root

    else:
        return left or right