'''
If we do bfs traversal in complete tree we won't get any null value after we hit out first null value.
Any function returns True is array has any true value else it returns null
'''

def completeTree(self,root):
    bfs = [root]
    i = 0
    while bfs[i]:
        bfs.append(bfs[i].left)
        bfs.append(bfs[i].right)

    return not any(bfs[i:])