class ListNode: 
    def __init__(self, val, nex=None, prev=None): 
        self.val = val 
        self.nex = nex
        self.prev = prev
    
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.nex = self.tail 
        self.tail.prev = self.head

        self.count = collections.defaultdict(int) # Counter for the actual queue
        self.mapping = {}

        for num in nums: 
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.head.nex is self.tail: 
            return -1
        return self.head.nex.val        

    def add(self, value: int) -> None:
        self.count[value] += 1

        if self.count[value] == 1:
            # append at tail
            prev = self.tail.prev
            node = ListNode(value, self.tail, prev)
            self.tail.prev = node
            prev.nex = node
            
            self.mapping[value] = node
        elif self.count[value] == 2: 
            # remove node 
            node = self.mapping[value]
            prev, nex = node.prev, node.nex
            prev.nex = nex
            nex.prev = prev
            del self.mapping[value]
        

        


        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)