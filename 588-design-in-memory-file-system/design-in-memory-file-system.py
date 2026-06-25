'''
if we use a hashmap then mkdir(/a/b/c) will need /a, /b, /c, /a/b, /b/c, /a/b/c

store directories in a tree structure

- ls(path): traverse path in tree starting from root. will end at the start of the required subtree - collect all items from this subtree 
- mkdir(path): traverse existing path in tree from root and create missing directories
- addContentToFile(filePath, content): use mkdir(filePath) to create that directory and attach content if newly created or else append 
- readContentFromFile(filePath): find the file and return the content 
'''

class TreeNode: 
    def __init__(self, name):
        self.name = name
        self.content = None 
        self.children = {}

class FileSystem:

    def __init__(self):
        self.root = TreeNode('')

    def find(self, path):
        curr = self.root 
        for name in self.parts(path): 
            if name not in curr.children:
                return None
            curr = curr.children[name]
        return curr

    def parts(self, path):
        return [p for p in path.split("/") if p]     

    def ls(self, path: str) -> List[str]:
        node = self.find(path)
        if node.content is not None:
            return [node.name]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        curr = self.root 
        for name in self.parts(path): 
            if name not in curr.children: 
                curr.children[name] = TreeNode(name)
            curr = curr.children[name]

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root 
        for name in self.parts(filePath): 
            if name not in curr.children: 
                curr.children[name] = TreeNode(name)
            curr = curr.children[name]
        if not curr.content: 
            curr.content = content 
        else: 
            curr.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        node = self.find(filePath)
        return node.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)