class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''
        problem: 
        - gene = 8 character long string (A, C, G, T)
        - mutation = 1 character changed
        - valid gene if in bank

        goal: return min number of mutations from start to end, -1 if none

        observations: 
        - undirected graph because AAAAAAAA -- AAAAAAAB
        - we need to find the min number of mutations i.e. min number of hops from start to end 
        

        approach: 
        - use bfs starting from start and 

        '''
        bank_set = set(bank)
        q = collections.deque([(0, startGene)]) # (mutations, gene)
        visited = {startGene}

        while q: 
            mutations, gene = q.popleft() 

            if gene == endGene:
                return mutations
            
            for i in range(len(gene)): 
                for char in ['A', 'C', 'G', 'T']:
                    nei_gene = gene[:i] + char + gene[i + 1:]
                    if nei_gene in bank_set and nei_gene not in visited: 
                        q.append((mutations + 1, nei_gene))
                        visited.add(nei_gene)
        return -1

        