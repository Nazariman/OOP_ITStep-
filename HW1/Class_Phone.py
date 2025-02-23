'''
Створіть клас Phone з атрибутами number та battery_level.
Додайте метод який зменшує заряд телефона(на скільки
зменшити відсотків передається як параметр), якщо він
опуститься нижче 20%, вивести повідомлення
Додайте метод для виведення інформації про телефон.
'''

class Phone: 
    def __init__ (self, number, battery_level = 100): 
        self.number = number
        self.battery_level = battery_level

class Phone:
    def __init__(self, number, battery_level=100):
        """Ініціалізація телефону з номером і рівнем заряду (за замовчуванням 100%)."""
        self.number = number
        self.battery_level = battery_level

    def decrease_battery(self, percent):
        if percent < 0:
            return "Значення не може бути від’ємним!"
        
        self.battery_level -= percent

        if self.battery_level < 0:
            self.battery_level = 0 

        if self.battery_level < 20:
            return f"Попередження: низький заряд ({self.battery_level}%)! Підключіть зарядний пристрій."
        
        return f"Заряд зменшено. Поточний рівень: {self.battery_level}%"

    def show_info(self):
        """Виводить інформацію про телефон."""
        return f"Телефон: {self.number}, Заряд: {self.battery_level}%"
