from classes.products import Electronics, Clothing,  Book
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
book = Book(name="Книга", price=500, author="Джордж Оруэлл", genre="Фантастика")

# Создаем пользователей
customer = Customer(username="Makism", email="python@derkunov.ru", address="033 Russ Bur")
admin = Admin(username="BOSS", email="root@derkunov.ru", admin_level=5)

# Создаем корзину покупок и добавляем товары
cart = ShoppingCart()
cart.add_item(laptop, 2, customer, admin)
cart.add_item(tshirt, 1, customer, admin)
cart.add_item(book, 2, customer, admin)

# Выводим детали корзины
print(cart.get_details())
