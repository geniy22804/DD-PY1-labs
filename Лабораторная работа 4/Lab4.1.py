
import json

def calculate_sum_of_products_from_file(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        total = 0.0
        for item in data:
            score = item.get('score', 0.0)
            weight = item.get('weight', 0.0)
            product = score * weight
            total += product

        return round(total, 3)

    except FileNotFoundError:
        print(f"Файл '{json_file_path}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка при чтении JSON файла '{json_file_path}'.")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

if __name__ == '__main__':
    json_file = 'input.json'

    total_sum = calculate_sum_of_products_from_file(json_file)

    if total_sum is not None:
        print(total_sum)
