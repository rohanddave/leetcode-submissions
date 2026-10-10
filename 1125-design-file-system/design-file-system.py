class FileSystem:

    def __init__(self):
        self.mapping = {}
        self.mapping['/'] = -1

    def createPath(self, path: str, value: int) -> bool:
        path_arr = path.split('/')[1:]
        parent_path = '/' + '/'.join(path_arr[:-1])
        if  parent_path not in self.mapping or path in self.mapping:
            return False 
        self.mapping[path] = value
        return True       

    def get(self, path: str) -> int:
        if path not in self.mapping:
            return -1
        return self.mapping[path]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)