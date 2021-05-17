'''
In this question we keep track of strings in path and when the one path is complete we delete it from the 
path array
'''

def smallestString(self,root):
    def dfs(node,path):
        if not node: return 
        path.append(chr(97+node.val))
        if not node.left and not node.right:
            res[0] = min(res[0], ''.join(path)[::-1])
        else:
            dfs(node.left,path)
            dfs(node.right,path)

        del path[-1]

    res = [str(chr(ord('z')+1))]
    dfs(root,[])
    return res[0]