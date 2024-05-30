# Предположим, что у нас есть словари, содержащие коэффициенты и процент брака для типов продукции и материалов

product_types = {
    1: {"name": "Тип продукции 1", "coefficient": 1.5},
    2: {"name": "Тип продукции 2", "coefficient": 2.0},
    3: {"name": "Тип продукции 3", "coefficient": 2.5}
}

material_types = {
    1: {"name": "Материал 1", "defect_rate": 0.05},  # 5% брака
    2: {"name": "Материал 2", "defect_rate": 0.1},   # 10% брака
    3: {"name": "Материал 3", "defect_rate": 0.15}   # 15% брака
}

def calculate_material(product_id, material_id, product_quantity, param1, param2):
    # Проверка существования типов продукции и материалов
    if product_id not in product_types or material_id not in material_types:
        return -1
    
    # Получение коэффициента продукции и процента брака материала
    product_coefficient = product_types[product_id]["coefficient"]
    material_defect_rate = material_types[material_id]["defect_rate"]
    
    # Расчет количества материала на одну единицу продукции
    material_per_product = param1 * param2 * product_coefficient
    
    # Общее количество материала для всего объема продукции
    total_material = material_per_product * product_quantity
    
    # Учет процента брака материала
    total_material_with_defect = total_material * (1 + material_defect_rate)
    
    # Округление до целого числа
    return int(total_material_with_defect)

# Вывод списка типов продукции и материалов
print("Доступные типы продукции:")
for id, info in product_types.items():
    print(f"{id}: {info['name']} (Коэффициент: {info['coefficient']})")

print("\nДоступные типы материалов:")
for id, info in material_types.items():
    print(f"{id}: {info['name']} (Процент брака: {info['defect_rate'] * 100}%)")

# Описание параметров продукции
print("\nПараметры продукции:")
print("param1: Длина продукции в метрах")
print("param2: Ширина продукции в метрах")

# Ввод данных от пользователя
try:
    product_id = int(input("\nВведите идентификатор типа продукции: "))
    material_id = int(input("Введите идентификатор типа материала: "))
    product_quantity = int(input("Введите количество получаемой продукции: "))
    param1 = float(input("Введите длину продукции (в метрах): "))
    param2 = float(input("Введите ширину продукции (в метрах): "))
    
    # Вызов функции для расчета необходимого материала
    required_material = calculate_material(product_id, material_id, product_quantity, param1, param2)
    
    if required_material == -1:
        print("Ошибка: введены некорректные данные.")
    else:
        print(f"Необходимое количество материала: {required_material}")
except ValueError:
    print("Ошибка: введены некорректные данные. Пожалуйста, убедитесь, что все вводимые значения корректны.")