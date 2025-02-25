from Class_BankAccount import BankAccount

# Тестування класу
account = BankAccount("Олександр", 1000, "UAH")

# Вивід інформації
print(account.show_info())

# Поповнення рахунку
print(account.deposit(500))

# Зняття коштів
print(account.withdraw(300))

# Конвертація валюти
print(f"Конвертація 500 UAH в EUR: {account.convert_currency(500, 'UAH', 'EUR')} EUR")

# Зміна валюти рахунку
print(account.change_currency("EUR"))

# Вивід оновленої інформації
print(account.show_info())