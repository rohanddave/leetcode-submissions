class UnionFind: 
    def __init__(self, n): 
        self.components = n 
        self.parent = list(range(n))
        self.size = [1] * n 
    
    def find(self, x): 
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y): 
        px, py = self.find(x), self.find(y) 
        if px == py: 
            return False
        
        if self.size[px] < self.size[py]: 
            px, py = py, px 
        self.parent[py] = px 
        self.size[px] += self.size[py]
        self.components -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''
        goal: return max edges you can remove to keep graph fully traversible by alice and bob 

        observations: 
        - bidirectional edges i.e. undirected graph 
        - graph can start off being not fully traversible by either or both 
        - assuming graph is fully traversible: we can only remove redundant connections
            redundant connection = an edge that is connecting 2 nodes that are connected directly or indirectly 
        - in a uf every node must have a parent
        
        approach: 
        - use union find to get connectivity between two nodes in almost constant time (inverse ackerman constant)
        - create two UFs: one for alice and one for bob
        - sort edges by type so that we include type 3 before any other edge
        - for each edge:
            if type 3 and not alice.union(u, v) and not bob.union(u, v):
                count += 1
            elif type 1 and not alice.union(u, v):
                count += 1
            elif type 2 and not bob.union(u, v):
                count += 1
        - we still need to check if both graphs are fully traversible
            if each node does not belong to the same component then not fully traversible => return -1
            else => return count
        '''
        alice = UnionFind(n)
        bob = UnionFind(n)

        edges.sort(key=lambda x: -x[0])
        count = 0
        for edge_type, u, v in edges: 
            u -= 1
            v -= 1
            
            if edge_type == 3: 
                alice_used = alice.union(u, v) 
                bob_used = bob.union(u, v)
                if not alice_used and not bob_used:
                    count += 1
            elif edge_type == 1 and not alice.union(u, v):
                count += 1
            elif edge_type == 2 and not bob.union(u, v):
                count += 1

        return -1 if alice.components != 1 or bob.components != 1 else count