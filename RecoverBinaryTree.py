'''
This question can be done in two ways
'''

'''
First way is of using simple inorder recurrsion, space complexity is o(n)
'''

def recoverBST1(self,root):
    self.first,self.second,self.prev = None,None,TreeNode(float('-inf'))

    def inorder(node):
        if node.left:
            inorder(node.left)

            if self.prev.val<node.val:
                self.first = self.first or self.prev
                self.second = node
            self.prev = node
            inorder(node.right)

    inorder(root)
    self.first.val,self.second.val = self.second.val,self.first.val



'''
Second Way is Using Morris Traversal: To traverse anny tree without using additional memory, morris traversal
is used
'''

def recoverBST2(self,root):
    curr,node,swap = root,TreeNode(float('-inf')),[]

    while curr:
        if curr.left:
            pre  = curr.left
            while pre.right and pre.right!=curr:
                pre = pre.right
            if not pre.right:
                pre.right = curr
                curr = curr.left
            else:
                if curr.val<node.val:
                    swap += [node,curr]
                node = curr
                curr = curr.right
        else:
            if curr.val<node.val:
                swap += [node,curr]
            node = curr
            curr = curr.right

    swap[0].val ,swap[-1].val = swap[-1].val,swap[0].val

            