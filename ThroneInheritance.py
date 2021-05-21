import collections
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.throne = collections.defaultdict(list)
        self.king = kingName
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.throne[parentName].append[childName]

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.ans = []
        def dfs(curr):
            if curr not in self.dead:
                self.ans.append(curr)

            for child in self.throne[curr]:
                dfs(child)

        dfs(self.king)
        return self.ans

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()