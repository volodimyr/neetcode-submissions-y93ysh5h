class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.customers = []

    def subscribe(self, observer: Observer) -> None:
        self.customers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.customers.remove(observer)
        

    def updateStock(self, newStock: int) -> None:
        org = self.stock
        self.stock = newStock
        if org == 0 and newStock > 0:
            for c in self.customers:
                c.notify(self.itemName)
        
