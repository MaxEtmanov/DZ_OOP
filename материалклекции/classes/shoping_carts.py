# 3. Класс для управления корзиной покупок

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity, customer, admin):
        self.items.append({"Продукт": product, "количество": quantity, "Клиент": customer, "Админ": admin})


    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self):
        details = "Корзинга пуста:\n"
        
        for item in self.items:
            product = item["Продукт"]
            quantity = item["количество"]
            customer = item["Клиент"]
            admin = item["Админ"]
            
            details +=(f"Покупатель {customer.username} приобрел {product.name} в количестве {quantity} шт. {item['Продукт'].get_details()} \n")
        
        details += f"Общая сумма: {self.get_total()} руб. Зарегистрировал покупки администратор {admin.username}."
        
        return details

