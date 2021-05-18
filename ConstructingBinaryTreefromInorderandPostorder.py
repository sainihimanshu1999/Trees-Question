'''
In this question we just have to use preorder array to get the index of elements and use that index in 
inorder array to make nodes
'''

def buildTree(self,inorder,postorder):
    if inorder:
        index = inorder.index(postorder.pop())
        node = TreeNode(inorder[index])
        node.right = self.buildTree(inorder[index+1:],postorder)
        node.left = self.buildTree(inorder[:index],postorder)
        return node