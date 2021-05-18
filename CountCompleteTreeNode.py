'''
In this question we are given a complete tree and we have to use this to our advantange, in complete 
binary tree max number of node are equal to 2**h where h is the height of the tree, we check depth of 
left and right subtree and if they are equal we recurr in root.right else we recurr in root.left
'''

def countNodes(self,root):
    if not root: return 0

    leftD = self.getDepth(root.left)
    rightD =  self.getDepth(root.right)

    if leftD == rightD:
        return pow(2,leftD) + self.countNodes(root.right)
    else:
        return pow(2,rightD) + self.countNodes(root.left)

def getDepth(self,root):
    if not root: return 0

    return 1 + self.getDepth(root.left)