'''
We have to conver path into numbers and then add them all to give final result
'''

def sumNums(self,root):
    if not root: return 0

    if not root.left and not root.right:
        return int(root.val)

    if root.left: root.left.val = 10*root.val + root.left.val
    if root.right: root.right.val = 10*root.val + root.right.val

    return self.sumNums(root.left)+self.sumNums(root.right)