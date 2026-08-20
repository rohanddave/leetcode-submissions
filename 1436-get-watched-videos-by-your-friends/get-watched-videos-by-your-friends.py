class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:       
        q = collections.deque([(id, 0)])
        visited = {id}
        videos_freq = collections.defaultdict(int)
        while q:
            person_id, dist = q.popleft()

            if dist == level:
                for video in watchedVideos[person_id]:
                    videos_freq[video] += 1
            else: 
                for nei_person in friends[person_id]:
                    if nei_person not in visited: 
                        visited.add(nei_person)
                        q.append((nei_person, dist + 1))
        
        ordered = sorted(videos_freq.items(), key=lambda x: (x[1], x[0]))
        return [video for video, freq in ordered]
