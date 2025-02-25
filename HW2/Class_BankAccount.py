'''
Напишіть клас Банківський рахунок з атрибутами:
 ім'я клієнта
 баланс
 валюта
 словник з курсом валют(однаковий для всіх)
Додайте методи:
 вивід загальної інформації
 перевірка чи відома валюта(якщо ні, викликати
ValueError)
 перевести гроші з однієї валюти в іншу(ця операція
часто використовується, тому зрочно реалізувати
окремим методом)
 зміна валюти
 поповнення балансу(валюта та сама)
 зняття грошей з балансу(валюта та сама).
'''

class BankAccount: 
    
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.96,
        "UAH": 41.7,
        "GBP": 0.79
    }
    
    def __init__ (self, name,  balance, currency): 
        self.name = name
        self.balance = balance
        self.currency = currency.upper()
        
        self.validate_currency(self.currency)
        
    def validate_currency(self, currency):
        if currency.upper() not in self.__class__.exchange_rates:
            raise ValueError(f"Валюта {currency} не підтримується")
    
    def show_info(self): 
        return f"Клієнт: {self.name}\n Баланс: {self.balance} {self.currency}\n"

    def deposit(self, amount): 
        if amount <= 0: 
            return "Сума поповнення повина бути більше 0!"
        self.balance += amount
        
        return f"Баланс поповнено на {amount} {self.currency}. Поточний баланс: {self.balance} {self.currency}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Сума має бути більше нуля!"
        if amount > self.balance:
            return "Недостатньо коштів на рахунку!"
        
        self.balance -= amount
        
        return f"Знято {amount} {self.currency}. Поточний баланс: {self.balance} {self.currency}"
    
    def convert_currency (self, amount, from_currency, to_currency): 
        self.validate_currency(from_currency)
        self.validate_currency(to_currency)
        
         # Конвертуємо в долари (як базову валюту)
        amount_in_usd = amount / self.exchange_rates[from_currency.upper()]
        # Конвертуємо з доларів у цільову валюту
        converted_amount = amount_in_usd * self.exchange_rates[to_currency.upper()]    
        
        return round(converted_amount, 2)
    
    def change_currency(self, new_currency):
        new_currency = new_currency.upper()
        self.validate_currency(new_currency)

        if new_currency == self.currency:
            return f"Рахунок вже у валюті {new_currency}."

        old_balance = self.balance
        old_currency = self.currency

        self.currency = new_currency
        self.balance = self.convert_currency(old_balance, old_currency, new_currency)

        return f"Валюта змінена: {old_balance} {old_currency} → {self.balance} {new_currency}"
