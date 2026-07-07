# Проект FitLife - MVP версия 1.0
# Константы для неизменяемых мер величин
WATER_PER_KG = 30
WATER_ON_LITTER = 1000

# Линия для визуального отделения
print("=" * 60)
# 1. Знакомство
user_name = input('Как вас зовут? ')


# 2. Сбор данных
# Ввод данных и проверка на тип
# и значение меньше или равное нулю
# Цикл подсказал и конструкцию проверки ИИ практикума
while True:
    try:
        user_age = int(input('Введите ваш возраст (пр.: 45): '))
        if user_age <= 0:
            print('Значение должно быть больше 0')
            continue
        else:
            print('=' * 60)
            break
    except ValueError:
        print('Пожалуйста, введите обычное число!')

while True:
    try:
        user_weight = float(input('Ваш вес в КГ (пр.: 40.5 или 40): '))
        if user_weight <= 0:
            print('Значение должно быть больше 0')
            continue
        else:
            print('=' * 60)
            break
    except ValueError:
        print('Пожалуйста, введите обычное число!')

while True:
    try:
        user_height = float(input('Ваш рост в метрах (пр.: 1.65 / 2): '))
        if user_height <= 0:
            print('Значение должно быть больше 0')
            continue
        else:
            print('=' * 60)
            break
    except ValueError:
        print('Пожалуйста, введите обычное число!')

# 3. Логика расчетов
# Индекс массы тела
bmi = user_weight / (user_height**2)
# Необходимое количество воды
water_needed = (user_weight * WATER_PER_KG) / WATER_ON_LITTER

# 4. Вывод результата
print(f'Привет, {user_name}!')
print(f'Ваш возраст {user_age} (лет/года)')
print(f'ИМТ: {round(bmi, 2)}')
print(f'Рекомендуемая норма воды: {round(water_needed, 1)} л. в день')
print('Расчет окончен. Будьте здоровы!')
