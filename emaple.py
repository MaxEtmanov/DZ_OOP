from classes.order import Order
from classes.product import Product
from classes.customer import Customer
from classes.discount import Discount

product1 = Product("IPhone", 1000)
product2 = Product("Computer", 2000)
product3 = Product("Mouse", 100)

order = Order([product1, product3])
order2 = Order([product2, product3])
order3 = Order([product1, product2])

discount = Discount("Скидка на првую покупку ", 15)
discount_2 = Discount("Скидка постоянного клиента ", 5)
discount_3 = Discount("Скидка в день рождение", 20)

sale_order = order.calculator_discounted_price((product1.price + product3.price),discount)
sale_order2= order2.calculator_discounted_price((product2.price + product3.price),discount_2)
sale_order3= order3.calculator_discounted_price((product1.price + product2.price),discount_3)

firsr_customer = Customer("Ivan", [sale_order])
second_customer = Customer("Petr", [sale_order2])
third_customer = Customer("Sidor", [sale_order3])



print(f"Всего заказов: {Order.total_orders()}")
total_sum = Order.total_price(order) + Order.total_price(order2) + Order.total_price(order3)
print(f"Общая сумма заказов: {total_sum}")



print(firsr_customer, discount)
print(second_customer, discount_2)
print(third_customer, discount_3)

print(product1)
print(product2) 
print(product3)

