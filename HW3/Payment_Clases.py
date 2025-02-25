'''
Створіть наступні класи:
 CreditCardPayment – атрибути currency
 PayPalPayment – атрибути currency
 CryptoPayment – атрибути currency
Методи:
 pay(amount) – виводить повідомлення
o CreditCardPayment – оплата карткою {amount}{currency}
o PayPalPayment – оплата PayPal {amount}{currency}
o CryptoPayment – оплата криптогаманцем {amount}{currency}
Напишіть функцію create_payment() яка запитує у
користувача тип рахунку та потрібні атрибути і повертає
об’єкт.
Створіть декілька рахунків, добавте їх у список та для
кожної викличте відповідні методи.

'''

class CreditCardPayment():
    def __init__ (self, currency):
        self.currency = currency.upper()
        
    def pay(self, amount):
        print(f"Оплата карткою: {amount} {self.currency}") 
        

class PayPalPayment(): 
    def __init__ (self, currency):
        self.currency = currency.upper()
        
    def pay(self, amount):
        print(f"Оплата через PayPal: {amount} {self.currency}")
        

class CryptoPayment(): 
    def __init__ (self, currency):
        self.currency = currency.upper()
        
    def pay(self, amount):
        print(f"Оплата криптовалютою: {amount} {self.currency}")
        
def create_payment():
    payment_type = input("Введіть тип платежу (CreditCard, PayPal, Crypto): ").strip().lower()
    currency = input("Введіть валюту платежу (USD, EUR, BTC тощо): ").strip().upper()
    
    if payment_type == "creditcard":
        return CreditCardPayment(currency)
    elif payment_type == "paypal":
        return PayPalPayment(currency)
    elif payment_type == "crypto":
        return CryptoPayment(currency)
    else:
        print("Невідомий тип платежу! Спробуйте ще раз.")
        return None
    
    
payments = []

# Створюємо кілька платежів вручну
payments.append(CreditCardPayment("USD"))
payments.append(PayPalPayment("EUR"))
payments.append(CryptoPayment("BTC"))

# Додаємо платіж, який створює користувач
user_payment = create_payment()
if user_payment:
    payments.append(user_payment)

# Викликаємо метод pay() для кожного платежу
for payment in payments:
    payment.pay(100)  # Наприклад, оплата 100 одиниць валюти