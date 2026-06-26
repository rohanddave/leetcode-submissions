class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.LOG = n.bit_length()
        self.up = [[-1] * self.LOG for _ in range(n)] # self.up[node][j] is the 2^jth ancestor of node

        # base case up[node][0] = up[node]
        for node in range(n): 
            self.up[node][0] = parent[node]
        
        for j in range(1, self.LOG): 
            for node in range(n):
                mid = self.up[node][j - 1]
                if mid != -1:
                    self.up[node][j] = self.up[mid][j - 1]


    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.LOG):
            if (k >> j) & 1:
                node = self.up[node][j]
                if node == -1:
                    return -1
        return node
                
            
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)