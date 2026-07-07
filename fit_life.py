# Проект FitLife - MVP версия 1.0
# Константы для неизменяемых мер величин
WATER_PER_KG = 30
WATER_ON_LITTER = 1000

# Линия для визуального отделения
print("=" * 60)
# 1. Знакомство
user_name = input('Как вас зовут? ')


# 2. Сбор данных
# Функция для проверки числа, с передачей аргументов
# 1 аргумент - подсказка, 2 аргумент - тип данных
# Основу взял у ии практикума, дополнил на основе гайдов из интернета
def check_number(hint, number_type):
    """Вычисляет тип ввода пользователя"""
    while True:

        try:
            number = number_type(input(hint))
            if number <= 0:
                print('Значение должно быть больше 0')
                continue
            else:
                print('=' * 60)
                return number
        except ValueError:
            print('Пожалуйста, введите обычное число!')


# объявление переменных для расчетов с вызовом функции
user_age = check_number('Введите ваш возраст (пр.: 45): ', int)
user_weight = check_number('Ваш вес в КГ (пр.: 40.5 или 40): ', float)
user_height = check_number('Ваш рост в метрах (пр.: 1.65 / 2): ', float)

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
