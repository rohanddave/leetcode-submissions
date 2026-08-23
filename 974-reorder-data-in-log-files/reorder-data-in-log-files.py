class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        problem: 
        - letter logs and digit logs 
        - letter logs before digit logs 
        - letter logs sorted lexicographically by content; if same then identifier
        - digit logs maintain relative ordering 

        observations: 
        - length of each log could be different 
        - identifiers are of different lengths too

        approach: 
        - 
        
        '''

        def extract(log): 
            res = []
            curr = ''

            i = 0 
            while i < len(log):
                if log[i] == ' ':
                    res.append(curr)
                    curr = ''
                
                if len(curr) == 2:
                    return res
                
                curr += log[i]
            return []
        
        digit_logs = [] 
        letter_logs = []
        heap = []

        for log in logs: 
            # identifier, first = extract(log)
            log_arr = log.split(' ')
            if log_arr[1].isnumeric(): 
                digit_logs.append(log)
            else: 
                heapq.heappush(heap, (log_arr[1:], log_arr[0], log))
        
        while heap: 
            content, identifier, log = heapq.heappop(heap)
            letter_logs.append(log)

        return letter_logs + digit_logs


