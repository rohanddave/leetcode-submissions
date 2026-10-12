class OrderManagementSystem:

    def __init__(self):
        self.mapping = {}
        self.secondary = collections.defaultdict(set)

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        self.mapping[orderId] = (orderType, price)    
        self.secondary[(orderType, price)].add(orderId)

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        o_type, o_price = self.mapping[orderId]
        self.secondary[(o_type, o_price)].remove(orderId)
        self.mapping[orderId] = (self.mapping[orderId][0], newPrice)    
        self.secondary[(o_type, newPrice)].add(orderId)        

    def cancelOrder(self, orderId: int) -> None:
        o_type, o_price = self.mapping.pop(orderId)
        self.secondary[(o_type, o_price)].remove(orderId)
        
    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        return list(self.secondary[(orderType, price)])
        


# Your OrderManagementSystem object will be instantiated and called as such:
# obj = OrderManagementSystem()
# obj.addOrder(orderId,orderType,price)
# obj.modifyOrder(orderId,newPrice)
# obj.cancelOrder(orderId)
# param_4 = obj.getOrdersAtPrice(orderType,price)