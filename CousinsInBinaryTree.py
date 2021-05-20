'''
Cousins are those nodes which are at same depth but have different parents
'''

def cousins(self,root):
    def dfs(node,parent,depth,target):
        if node:
            if node.val == target:
                return depth,parent
            return dfs(node.left,node,depth+1,target) or dfs(node.right,node,depth+1,target)
    dx,px,dy,py = dfs(root,None,0,x)+def(root,None,0,y)
    return dx==dy  and px!=py