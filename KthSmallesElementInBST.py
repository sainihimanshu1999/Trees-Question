'''
we have to find kth smallest element in the tree
'''

def kthSmallestElement(self,root):
    x = []
    def ino(node):
        if node:
            ino(node.left)
            x.append(node.val)
            ino(node.right)

    ino(root)
    return x[k-1]
