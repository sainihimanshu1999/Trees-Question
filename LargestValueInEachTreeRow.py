'''
This question can be done by two Methods, BFS and DFS method
'''

#BFS

def largestVal(self,root):
    self.ans = []
    q = [root]
    
    while q:
        level = []
        for i in range(len(q)):
            node = q.pop()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

            level.append(node.val)
        self.ans.append(max(level))

    return self.ans



#DFS

def largestVal2(self,root):
    self.result = []

    def dfs(node,level):
        if not node: return None

        if len(self.result) == level:
            self.result.append(node.val)

        else:
            self.result[level] = max(self.result[level],node.val)

        dfs(node.left,level+1)
        dfs(node.right,level+1)

    dfs(root,0)
    return self.result