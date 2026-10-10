class TreeNode: 
    def __init__(self, value = -1): 
        self.value = value
        self.children = {}

class FileSystem:

    def __init__(self):
        self.root = TreeNode()        

    def createPath(self, path: str, value: int) -> bool:
        curr = self.root 
        path_arr = path.split('/')[1:]
        for p in path_arr[:-1]:
            if p not in curr.children: 
                return False
            curr = curr.children[p]
        if path_arr[-1] in curr.children:
            return False
        curr.children[path_arr[-1]] = TreeNode(value)
        return True        

    def get(self, path: str) -> int:
        curr = self.root 
        for p in path.split('/')[1:]:
            if p not in curr.children:
                return -1
            curr = curr.children[p]
        return curr.value

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)