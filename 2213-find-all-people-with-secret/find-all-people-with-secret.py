class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        '''
        approach: 
        - sort by time 
        - for each time t create an undirected graph of meetings x -- y 
        - maintain a set of people with secret 
        - run a multi source dfs starting from each person with secret for graph in every time t
        '''
        meetings.sort(key=lambda x: x[2])
        graphs = {}
        graphs[0] = collections.defaultdict(list)
        graphs[0][0].append(firstPerson)
        graphs[0][firstPerson].append(0)
        people_with_secret = {0, firstPerson}

        times = []

        for x, y, t in meetings: 
            if not times or times[-1] != t:
                times.append(t)
            if t not in graphs: 
                graphs[t] = collections.defaultdict(list)
            graphs[t][x].append(y)
            graphs[t][y].append(x)

        for t in times: 
            adj = graphs[t]
            q = collections.deque()
            for person in adj: 
                if person in people_with_secret:
                    q.append(person)
            while q: 
                person = q.popleft() 

                for nei_person in adj[person]:
                    if nei_person not in people_with_secret: 
                        q.append(nei_person)
                        people_with_secret.add(nei_person)
        return list(people_with_secret)