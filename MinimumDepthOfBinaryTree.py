'''
This question is similar to max depth of binary tree, we just have to keep corner cases in mind
'''

def minDepth(self,root):
    if not root: return 0

    if root.left and not root.right:
        return 1+self.minDepth(root.left)
    
    if root.right and not root.left:
        return 1+self.minDepth(root.right)

    return 1+min(self.minDepth(root.right),self.minDepth(root.left))