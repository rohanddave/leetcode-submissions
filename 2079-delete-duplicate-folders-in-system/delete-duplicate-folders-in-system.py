class TreeNode: 
    def __init__(self, value):
        self.value = value 
        self.children = {}
    
    def __lt__(self, other):
        return self.value < other.value
    
class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        '''
        problem: 
        - identical: same non-empty set of subfolders 
        - not necessarily at the root level to be identical 
        - two or more flders identical mark the folders as well as subfolders 

        goal: return 2d array containing non identical folders in any order 
        '''
        # build trie
        root = TreeNode('')
        for path in paths: 
            curr = root
            for directory in path: 
                if directory not in curr.children:
                    node = TreeNode(directory)
                    curr.children[directory] = node
                curr = curr.children[directory]
        
        # identify duplicates
        folders = collections.defaultdict(list)

        def dfs(node): 
            serializable_postorder = tuple(
                (child_name, dfs(child_node))
                for child_name, child_node in sorted(node.children.items())
            ) 
            
            if serializable_postorder:
                folders[serializable_postorder].append(node)
            return serializable_postorder
        
        # compute postorders for duplicates
        dfs(root)

        # find nodes to delete
        nodes_to_delete = set() 
        for nodes in folders.values(): 
            if len(nodes) > 1: 
                nodes_to_delete.update(nodes) 
        
        # compute result
        res = []
        def dfs2(node, path):
            # short circuit - skip entire subtree
            if node in nodes_to_delete:
                return

            # only add to path if not root
            if node is not root:  
                path.append(node.value)
            
            # if there is a path append to res
            if path:
                res.append(path[:])
            
            # recursively traverse children
            for child in node.children.values():
                dfs2(child, path)
            
            # backtrack - same condition as adding to path
            if node is not root:
                path.pop()
        
        # compute res
        dfs2(root, [])
        return res

        