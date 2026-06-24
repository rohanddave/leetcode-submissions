class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        for a, b in edges: 
            in_degree[b] += 1
        
        res = [] 
        for node, in_deg in enumerate(in_degree): 
            if in_deg == 0:
                res.append(node)

        return res
        