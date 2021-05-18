'''
This question was pretty hard, you have to make a dictionary and need to group having same column 
together, then append it into the output
'''


import collections


def verticalOrder(self,root):
    self.min_l,self.max_l = float('inf'),float('inf')
    dic = collections.defaultdict(list)

    def dfs(node,col,row):
        self.min_l = min(self.min_l,col)
        self.max_l = max(self.max_l,col)
        dic[col].append((row,node.val))
        if node.left: dfs(node.left,col-1,row+1)
        if node.right: dfs(node.right.col+1,row+1)

    result = []
    for i in range(self.min_l,self.max_l+1):
        result += [[j for i,j in sorted(dic[i])]]
    return result