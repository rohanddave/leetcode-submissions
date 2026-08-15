class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        '''
        problem:
        - invocations[i] = [a, b] where a calls b i.e. b depends on a
        - bug in method k
        - remove all methdos that directly or indirectly calls method k 
        - group of methods can be removed if no method outside the group invokes any methods within it

        goal: return array containing remaining methods after removing sus. if not possible to remove all sus none should be removed

        observations: 
        - methods reachable from k are sus and need to be removed
        - a method can be removed only if none (outide it's reachable group)invoke it
        - cycles are possible

        example: 

        '''

        adj = collections.defaultdict(list) 
        for a, b in invocations: 
            adj[a].append(b)
        
        q = collections.deque([k])
        visited = {k}

        while q: 
            method = q.popleft() 

            for nei_method in adj[method]: 
                if nei_method not in visited: 
                    q.append(nei_method)
                    visited.add(nei_method)
        
        for a, b in invocations:
            if a not in visited and b in visited:
                return list(range(n))
        
        return list(set(list(range(n))) - visited)
        
            

        