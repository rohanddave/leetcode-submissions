class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = [(-priority, -task_id, user_id) for user_id, task_id, priority in tasks]
        heapq.heapify(self.heap)

        self.task_to_priority_map = {} 
        for user_id, task_id, priority in tasks: 
            self.task_to_priority_map[task_id] = (priority, user_id)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, (-priority, -taskId, userId))
        self.task_to_priority_map[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        _, user_id = self.task_to_priority_map[taskId]
        self.task_to_priority_map[taskId] = (newPriority, user_id)

        heapq.heappush(self.heap, (-newPriority, -taskId, user_id))

    def rmv(self, taskId: int) -> None:
        self.task_to_priority_map.pop(taskId)

    def execTop(self) -> int:
        while self.heap: 
            neg_priority, neg_task_id, user_id = heapq.heappop(self.heap)
            priority, task_id = -neg_priority, -neg_task_id

            if task_id in self.task_to_priority_map and self.task_to_priority_map[task_id] == (priority, user_id):
                self.task_to_priority_map.pop(task_id)
                return user_id
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()