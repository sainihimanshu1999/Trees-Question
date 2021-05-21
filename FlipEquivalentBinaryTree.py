'''
In this question we have to check if two binary trees can be made equivalent by fipping
'''

def flip(self,root1,root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2: return False

    if not root1.val != root2.val : return False

    return (self.flip(root1.left,root2.left)and self.flip(root1.right,root2.right)) or(self.flip(root1.left,root2.right) and self.flip(root1.right,root2.left))