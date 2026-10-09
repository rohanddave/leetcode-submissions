class UnionFind: 
    def __init__(self, n):
        self.size = [1] * n 
        self.parent = list(range(n))
        self.components = n
    
    def find(self, x): 
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y): 
        px, py = self.find(x), self.find(y)
        if px == py:
            return False 
        
        if px > py: 
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        return True
    
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)

        for x, y in connections:
            uf.union(x - 1, y - 1)
        
        min_heap_map = collections.defaultdict(list)
        for station in range(c): 
            parent = uf.find(station)
            heapq.heappush(min_heap_map[parent], station)
            
        non_operational = set() 

        def get_servicing_station(x):
            nonlocal c
            if x not in non_operational:
                return x + 1
            
            parent = uf.find(x)
            heap = min_heap_map[parent]
            if not heap:
                return -1
            
            while heap and heap[0] in non_operational:
                heapq.heappop(heap)
            
            return -1 if not heap else heap[0] + 1
        
        res = []
        
        for req_type, station in queries: 
            if req_type == 1:
                res.append(get_servicing_station(station - 1))
            else:
                non_operational.add(station - 1)
        
        return res