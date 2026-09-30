class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        '''
        observations: 
        - alert if worker uses key card three or more times in an hour

        approach: 
        - zip keyName with keyTime
        - sort according to keyTime, (maybe keyName??)
        - maintain a hashmap {name: deque()}
        - deque contains (timestamp)
        - each deque only contains timestamps in the last hour
            - shrink till window is an hour only
            - then insert new timestamp 
            - if length >= 3 insert into res 
        - return sorted res
        '''

        def get_timestamp(key_time_str): 
            hour_str, min_str = key_time_str.split(':')
            return int(hour_str) * 60 + int(min_str)
        
        zipped = [(get_timestamp(keyTime[i]), keyName[i]) for i in range(len(keyName))]

        mapping = collections.defaultdict(collections.deque)
        res = set()

        for timestamp, name in sorted(zipped):
            while len(mapping[name]) > 0 and timestamp - mapping[name][0] > 60: 
                mapping[name].popleft() 
            
            mapping[name].append(timestamp)

            if len(mapping[name]) >= 3:
                res.add(name)

        return sorted(res)