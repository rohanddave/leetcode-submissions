class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        call_stack = []
        prev_timestamp = 0
        res = [0] * n

        for log in logs: 
            func_id, event, timestamp = log.split(':')
            func_id = int(func_id)
            timestamp = int(timestamp)

            if event == 'start':
                if call_stack: 
                    res[call_stack[-1]] += timestamp - prev_timestamp
                call_stack.append(func_id)
                prev_timestamp = timestamp
            else: 
                res[call_stack[-1]] += timestamp - prev_timestamp + 1
                call_stack.pop()
                prev_timestamp = timestamp + 1
        
        return res

        