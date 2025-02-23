#1
from Class_Cart import Cart  # Імпортуємо клас Cart

# Створюємо об'єкт класу
cart = Cart("Олександр")

# Додаємо товари
cart.add_item("Ноутбук")
cart.add_item("Смартфон")

# Виводимо інформацію про кошик
print(cart.show_cart())  # Кошик клієнта: Олександр, товари: Ноутбук, Смартфон

# Видаляємо товар і виводимо повідомлення
message = cart.remove_item("Ноутбук")
print(message)  # Усі товари 'Ноутбук' видалено з кошика.

# Показуємо оновлений кошик
print(cart.show_cart())  # Кошик клієнта: Олександр, товари: Смартфон


#2 
from Class_Phone import Phone

phone = Phone("+380501234567")

print(phone.show_info())  

# Зменшуємо заряд
print(phone.decrease_battery(30))  
# Зменшуємо ще, щоб перевірити попередження
print(phone.decrease_battery(55))  
# Виводимо фінальний стан телефону
print(phone.show_info())  