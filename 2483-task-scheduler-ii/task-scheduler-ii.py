class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        '''
        goal: return min days to complete all tasks 

        tasks[i] = type of ith task 
        space = min days that must pass after to complete same task 

        observation: 
        - tasks need to completed in order 
        - each day can either schedule or take a break 
        
        approach: 
        - keep track of current day: day starts at 1
        - for each task
            - if task[i] cannot be scheduled today: move day to day it can be scheduled
            - move day by 1 (since now it can be scheduled)
            - hashmap[task[i]] = curr_day + space
        - we maintain a hashmap for each task type where {task_type: next day we can schedule}
        '''

        next_available = {}
        curr_day = 1
        for task in tasks: 
            if task in next_available and next_available[task] > curr_day:
                curr_day = next_available[task]
                del next_available[task]
            next_available[task] = curr_day + space + 1
            curr_day += 1
        
        return curr_day - 1

        