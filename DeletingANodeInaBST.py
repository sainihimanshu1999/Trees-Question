'''
This question was fairly easy
'''

def deletingNode(self,root,key):
    if not root: return None

    if root.val == key:
        if not root.left: return root.right
        if not root.right: return root.left

        if root.left and root.right:
            temp = root.right
            while temp.left:
                temp = temp.left

            root.val = temp.val
            root.right = self.deletingNode(root.right,root.val)

    elif root.val<key:
        root.right = self.deletingNode(root.right,key)
    else:
        root.left = self.deletingNode(root.left,key)

    return root