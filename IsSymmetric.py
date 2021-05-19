'''
In this question we have to see wheter the tree is symmetric or a mirror image of itself
'''

def symmetric(self,root):
    if not root: return True

    def isMirror(left,right):
        if not left and not right: return True

        if not left or not right: return False

        if left.val == right.val:
            inner = isMirror(left.right,right.left)
            outer = isMirror(left.left,right.right)

            return isMirror(inner) and isMirror(outer)
        else:
            return False

    return isMirror(root.left,root.right)