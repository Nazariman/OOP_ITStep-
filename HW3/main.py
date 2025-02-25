import Payment_Clases
# Список платежів
payments = []

# Створюємо кілька платежів вручну
payments.append(Payment_Clases.CreditCardPayment("USD"))
payments.append(Payment_Clases.PayPalPayment("EUR"))
payments.append(Payment_Clases.CryptoPayment("BTC"))

# Додаємо платіж, який створює користувач
user_payment = Payment_Clases.create_payment()
if user_payment:
    payments.append(user_payment)

# Викликаємо метод pay() для кожного платежу
for payment in payments:
    payment.pay(100)  # Наприклад, оплата 100 одиниць валюти