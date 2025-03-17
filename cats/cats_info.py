def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats_list.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Помилка обробки рядка: {line.strip()}")
                    continue
        return cats_list
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

# Приклад використання
path = r"C:\Users\26012\OneDrive\Робочий стіл\home_w\cats\cats_file.txt"

cats_info = get_cats_info(path)
print(cats_info)
