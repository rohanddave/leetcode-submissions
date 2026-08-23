class TreeNode: 
    def __init__(self, val):
        self.val = val 
        self.children = {}
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        '''
        approach:
        - return the nodes that are direct children of root folder
        '''
        root = TreeNode('')
        res = []

        for directory in sorted(folder): 
            folders = directory.split('/')[1:]
            is_sub_folder = False 

            curr = root 
            for f in folders: 
                if f in curr.children:
                    if curr.children[f].is_end:
                        is_sub_folder = True 
                        break 
                else:
                    curr.children[f] = TreeNode(f)
                curr = curr.children[f]
            
            
            if not is_sub_folder:
                curr.is_end = True
                res.append(directory)

        
        return res
            