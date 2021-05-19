def buildTree(self,inorder,preorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[index])
        node.left = self.BuildTree(inorder[:index],preorder)
        node.right = self.buildTree(inorder[index+1:,preorder])
        return node