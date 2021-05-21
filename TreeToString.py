'''
In this question we have to convert out tree to a sring with paranthesis
'''

def tree2str(self,root):
    
    if not root: return ''
    result = ''

    left = self.tree2str(root.left)
    right= self.tree2str(root.right)

    if left or right:
        result += '(%s)' % left

    if right:
        result += '(%s)' %right

    return str(root.val)+result