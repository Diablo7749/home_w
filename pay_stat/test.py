def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Помилка обробки рядка: {line.strip()}")
                    continue
            
            if not salaries:
                return 0, 0
            
            total = sum(salaries)
            average = total / len(salaries)
            return total, average
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

# Приклад використання
path = "C:/Users/26012/OneDrive/Робочий стіл/home_w/pay_stat/salary_file.txt"
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
