'''
Створіть клас Cart(кошик клієнта магазину) з атрибутами
client(ім’я клієнта) та items(список товарів).
Додайте метод який додає новий товар до кошика
Додайте метод який видаляє товар з кошика
Додайте метод для виведення інформації про кошик
'''

class Cart: 
    def __init__ (self, client): 
        self.client = client
        self.items = []
        
    def add_item(self, item): 
        self.items.append(item)
        return f"Товар {item} було додано до кошика"
        
    def remove_item(self, item): 
            if item in self.items: 
                self.items.remove(item)
                return f"{item} було видалено з списку"
            else: 
                return f"{item} не знайдено в списку"
    
    def show_cart(self):
        print(f"Кошик клієнта: {self.client}")
        if self.items:
            print("Товари у кошику:")
            for item in self.items:
                print(f" - {item}")
        else:
            return "Кошик порожній."
        