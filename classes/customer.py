class Customer:
    def __init__(self, name: str, order: str):
        self.name = name
        self.order = order
        
    def __str__(self):
        order_names = ', '.join(str(product) for product in self.order)
        return f"Покупатель (Имя = {self.name}, Заказ = {order_names})"
    
    
