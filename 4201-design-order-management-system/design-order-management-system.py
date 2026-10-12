class OrderManagementSystem:

    def __init__(self):
        self.mapping = {}

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        self.mapping[orderId] = (orderType, price)        

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        self.mapping[orderId] = (self.mapping[orderId][0], newPrice)       

    def cancelOrder(self, orderId: int) -> None:
        del self.mapping[orderId]
        
    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        res = [] 
        for orderId, (o_type, o_price) in self.mapping.items(): 
            if orderType == o_type and price == o_price:
                res.append(orderId)
        return res
        


# Your OrderManagementSystem object will be instantiated and called as such:
# obj = OrderManagementSystem()
# obj.addOrder(orderId,orderType,price)
# obj.modifyOrder(orderId,newPrice)
# obj.cancelOrder(orderId)
# param_4 = obj.getOrdersAtPrice(orderType,price)