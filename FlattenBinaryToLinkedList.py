'''
There are to wasy to flatten the binary tree to linked list, first method is using reverse preorder 
traversal and dfs and another method is using stack
'''

#first reverse dfs

def binaryLinked(self,root):
    self.prev = None
    def dfs(node):
        if not node: return None

        dfs(node.right)
        dfs(node.left)

        node.right = self.prev
        node.left = None
        self.prev = node
    dfs(root)


#second Method Stack

def binaryLinked2(self,root):
    last = TreeNode(-1)
    stack = [root]
    while stack:
        node = stack.pop()
        last.right = node
        last.left = None
        if node and node.right:
            stack.append(node.right)
        if node and node.left:
            stack.append(node.left)

        last = node
    