'''
In this question we havr to find the mode in binary tress , i.e the most frequently repeating element
'''
def mode(self,root):
    if not root.left and not root.right:
        return [root.val]

    self.mode = 0
    self.dic = {}
    result = []

    def ino(node):
        if node:
            ino(node.left)
            self.dic[node.val] = self.dic.get(node.val,0)+1
            self.mode = max(self.mode,self.dic[node.val])
            ino(node.right)


    for k,v in self.dic.items():
        if v == self.mode:
            result.append(k)

    return result