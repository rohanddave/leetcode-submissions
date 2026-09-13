class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        def does_overlap(a, b): 
            return not (a[0] > b[1] or a[1] < b[0])
        
        meetings.sort()
        merged = [meetings[0]] 
        available = [1, days]
        res = days

        for i in range(1, len(meetings)): 
            if does_overlap(merged[-1], meetings[i]):
                merged[-1][1] = max(meetings[i][1], merged[-1][1])
            else: 
                interval = merged[-1]
                intersection = [max(available[0], interval[0]), min(available[1], interval[1])]
                overlap = intersection[1] - intersection[0] + 1
                if overlap > 0:
                    res -= overlap
                merged.append(meetings[i])
        interval = merged[-1]
        intersection = [max(available[0], interval[0]), min(available[1], interval[1])]
        overlap = intersection[1] - intersection[0] + 1
        if overlap > 0:
            res -= overlap
        return res

