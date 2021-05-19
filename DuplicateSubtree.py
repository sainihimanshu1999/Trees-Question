'''
We solve this question using preorder traversal and simple dictionary
'''

def duplicate(self,root):
    if not root: return []
    self.dic = {}
    self.result = []
    self.preorder(root)
    return self.result


def preorder(self,node):
    if node:
        a = str(node.val)+'-'+self.preorder(node.left)+'-'+self.preorder(node.right)
        count = self.dic.get(a,0)
        if count == 1:
            self.result.append(a)
        self.dic[a] = count + 1
        return a
    else: return '#'