class TreeNode: 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = TreeNode((-1, -1))

    def book(self, startTime: int, endTime: int) -> bool:        
        def _helper(node, start, end): 
            if not node: 
                return TreeNode((start, end)), True
            
            did_insert = False
            if end <= node.val[0]:
                node.left, did_insert = _helper(node.left, start, end)
            elif start >= node.val[1]:
                node.right, did_insert = _helper(node.right, start, end)
            
            return node, did_insert
        
        _, res = _helper(self.root, startTime, endTime)
        return res

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)