class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName 
        self.children = collections.defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)        

    def death(self, name: str) -> None:
        self.dead.add(name)      

    def getInheritanceOrder(self) -> list[str]:
        res = [] 
        def dfs(person): 
            if person not in self.dead:
                res.append(person)
            for child in self.children[person]:
                dfs(child)

        dfs(self.king)
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()