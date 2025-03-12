# Завдання № 1
from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримання поточної дати
        today = datetime.today().date()
        # Розрахунок різниці у днях
        delta = today - input_date
        # Повернення різниці як ціле число
        return delta.days
    except ValueError:
        # Обробка помилки у випадку неправильного формату дати
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

# Приклади використання
print(get_days_from_today("2021-10-09"))  # Наприклад, 157
print(get_days_from_today("2023-12-25"))  # Інший приклад
print(get_days_from_today("2020-02-30"))  # Неправильна дата
# Завдання № 2
import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка коректності вхідних даних
    if not (1 <= min <= max <= 1000) or quantity > (max - min + 1):
        return []
    
    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Повернення відсортованого списку
    return sorted(numbers)

# Приклади використання
print(get_numbers_ticket(1, 49, 6))  # Наприклад, [3, 12, 25, 34, 42, 47]
print(get_numbers_ticket(1, 36, 5))  # Інший приклад
print(get_numbers_ticket(1, 10, 15))  # Поверне пустий список через помилку у quantity
# Завдання № 3
import re

def normalize_phone(phone_number):
    # Видалення всіх непотрібних символів, крім цифр і знака '+' на початку
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number.strip())
    
    # Перевірка наявності міжнародного коду
    if cleaned_number.startswith('+'):
        if not cleaned_number.startswith('+38') and cleaned_number[1:4] == '380':
            return '+' + cleaned_number[1:]  # Додаємо лише знак '+' перед '380'
        return cleaned_number  # Повернення номера з коректним міжнародним кодом
    
    # Якщо номер починається з '380' без знака '+'
    if cleaned_number.startswith('380'):
        return '+' + cleaned_number

    # Якщо номер без міжнародного коду
    return '+38' + cleaned_number

# Приклади використання
print(normalize_phone("    +38(050)123-32-34"))  # +380501233234
print(normalize_phone("     0503451234"))         # +380503451234
print(normalize_phone("(050)8889900"))            # +380508889900
print(normalize_phone("38050-111-22-22"))         # +380501112222
print(normalize_phone("38050 111 22 11   "))      # +380501112211