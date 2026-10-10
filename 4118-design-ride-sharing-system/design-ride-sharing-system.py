class RideSharingSystem:

    def __init__(self):
        self.rider_q = collections.deque() 
        self.driver_q = collections.deque()
        self.riders = set()  

    def addRider(self, riderId: int) -> None:
        self.rider_q.append(riderId)      
        self.riders.add(riderId)  

    def addDriver(self, driverId: int) -> None:
        self.driver_q.append(driverId)        

    def matchDriverWithRider(self) -> List[int]:
        if not self.rider_q or not self.driver_q:
            return [-1, -1]
        
        while self.rider_q and self.rider_q[0] not in self.riders:
            popped_rider = self.rider_q.popleft()
            

        if not self.rider_q: 
            return [-1, -1]
        
        riderId = self.rider_q.popleft()
        self.riders.remove(riderId)
        return [self.driver_q.popleft(), riderId]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riders:
            self.riders.remove(riderId)

        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)