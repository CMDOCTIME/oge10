import sys
from colorama import init, Fore, Style

# Инициализация colorama
init(autoreset=True)

def convert_to_decimal(number_str, base):
    """Функция для преобразования числа в десятичную систему счисления"""
    try:
        return int(number_str, base)
    except ValueError:
        return None

def solve_task_1():
    """Задача: Найти максимальное число среди чисел в разных системах счисления"""
    print(Style.BRIGHT + Fore.GREEN + "\n--- Задача 1: Найти максимальное число среди чисел в разных системах счисления ---" + Style.RESET_ALL)
    
    numbers = []
    bases = []
    
    for i in range(1, 4):
        num = input(f"Введите число {i}: ").strip()
        base_input = input(f"Введите основание системы счисления для числа {i}: ").strip()
        if not base_input.isdigit() or int(base_input) <= 1:
            print(Fore.RED + "Ошибка: Основание системы счисления должно быть целым числом больше 1." + Style.RESET_ALL)
            return
        base = int(base_input)
        numbers.append(num)
        bases.append(base)
    
    decimal_values = []
    for num, base in zip(numbers, bases):
        decimal_value = convert_to_decimal(num, base)
        if decimal_value is not None:
            decimal_values.append(decimal_value)
        else:
            print(Fore.RED + f"Ошибка: число {num} некорректно для основания {base}." + Style.RESET_ALL)
            return
    
    max_decimal = max(decimal_values)
    print(Style.BRIGHT + f"\nМаксимальное число в десятичной системе: {max_decimal}" + Style.RESET_ALL)

def solve_task_2():
    """Задача: Найти число с минимальным количеством единиц в двоичной записи"""
    print(Style.BRIGHT + Fore.GREEN + "\n--- Задача 2: Найти число с минимальным количеством единиц в двоичной записи ---" + Style.RESET_ALL)
    
    numbers = []
    for i in range(1, 4):
        num_input = input(f"Введите десятичное число {i}: ").strip()
        if not num_input.isdigit() or int(num_input) < 0:
            print(Fore.RED + "Ошибка: Введите корректное неотрицательное целое число." + Style.RESET_ALL)
            return
        num = int(num_input)
        numbers.append(num)
    
    def count_ones(n):
        return bin(n).count('1')
    
    min_ones_number = min(numbers, key=lambda x: count_ones(x))
    min_ones_count = count_ones(min_ones_number)
    print(Style.BRIGHT + f"\nЧисло с минимальным количеством единиц в двоичной записи: {min_ones_number}" + Style.RESET_ALL)
    print(f"Количество единиц в его двоичной записи: {min_ones_count}")

def solve_task_3():
    """Задача: Найти число с минимальной суммой цифр в восьмеричной записи"""
    print(Style.BRIGHT + Fore.GREEN + "\n--- Задача 3: Найти число с минимальной суммой цифр в восьмеричной записи ---" + Style.RESET_ALL)
    
    numbers = []
    for i in range(1, 4):
        num_input = input(f"Введите десятичное число {i}: ").strip()
        if not num_input.isdigit() or int(num_input) < 0:
            print(Fore.RED + "Ошибка: Введите корректное неотрицательное целое число." + Style.RESET_ALL)
            return
        num = int(num_input)
        numbers.append(num)
    
    def sum_octal_digits(n):
        return sum(int(digit) for digit in oct(n)[2:])
    
    min_sum_number = min(numbers, key=lambda x: sum_octal_digits(x))
    min_sum = sum_octal_digits(min_sum_number)
    print(Style.BRIGHT + f"\nЧисло с минимальной суммой цифр в восьмеричной записи: {min_sum_number}" + Style.RESET_ALL)
    print(f"Сумма цифр в его восьмеричной записи: {min_sum}")

def solve_task_4():
    """Задача: Найти наименьшее возможное основание системы счисления"""
    print(Style.BRIGHT + Fore.GREEN + "\n--- Задача 4: Найти наименьшее возможное основание системы счисления ---" + Style.RESET_ALL)
    
    number_str = input("Введите число (например, 3322): ").strip()
    if not number_str:
        print(Fore.RED + "Ошибка: Введена пустая строка." + Style.RESET_ALL)
        return
    
    def find_min_base(num_str):
        max_digit = 0
        for char in num_str:
            if char.isdigit():
                digit = int(char)
            elif char.isalpha():
                digit = ord(char.upper()) - ord('A') + 10
            else:
                return None
            if digit < 0:
                return None
            max_digit = max(max_digit, digit)
        return max_digit + 1
    
    min_base = find_min_base(number_str)
    if min_base is None or min_base < 2:
        print(Fore.RED + f"Ошибка: Некорректный ввод числа {number_str}." + Style.RESET_ALL)
        return
    
    decimal_value = convert_to_decimal(number_str, min_base)
    if decimal_value is not None:
        print(Style.BRIGHT + f"\nНаименьшее основание системы счисления: {min_base}" + Style.RESET_ALL)
        print(f"Число в десятичной системе: {decimal_value}")
    else:
        print(Fore.RED + f"Ошибка: число {number_str} не может быть переведено в десятичную систему для основания {min_base}." + Style.RESET_ALL)

def solve_task_5():
    """Задача: Найти наибольшее возможное основание системы счисления при ограничении"""
    print(Style.BRIGHT + Fore.GREEN + "\n--- Задача 5: Найти наибольшее возможное основание системы счисления при ограничении ---" + Style.RESET_ALL)
    
    number_str = input("Введите число (например, 121): ").strip()
    if not number_str:
        print(Fore.RED + "Ошибка: Введена пустая строка." + Style.RESET_ALL)
        return
    
    limit_input = input("Введите предел в десятичной системе (например, 108): ").strip()
    if not limit_input.isdigit() or int(limit_input) <= 0:
        print(Fore.RED + "Ошибка: Предел должен быть положительным целым числом." + Style.RESET_ALL)
        return
    limit = int(limit_input)
    
    def find_min_base(num_str):
        max_digit = 0
        for char in num_str:
            if char.isdigit():
                digit = int(char)
            elif char.isalpha():
                digit = ord(char.upper()) - ord('A') + 10
            else:
                return None
            if digit < 0:
                return None
            max_digit = max(max_digit, digit)
        return max_digit + 1
    
    def find_max_base(num_str, limit_val):
        min_base = find_min_base(num_str)
        if min_base is None:
            return None
        suitable_base = min_base
        for base in range(min_base, limit_val + 2):
            decimal_value = convert_to_decimal(num_str, base)
            if decimal_value is not None and decimal_value < limit_val:
                suitable_base = base
            else:
                break
        return suitable_base
    
    max_base = find_max_base(number_str, limit)
    if max_base is None:
        print(Fore.RED + f"Ошибка: Некорректный ввод числа {number_str}." + Style.RESET_ALL)
        return
    
    decimal_value = convert_to_decimal(number_str, max_base)
    if decimal_value is not None:
        print(Style.BRIGHT + f"\nНаибольшее основание системы счисления: {max_base}" + Style.RESET_ALL)
        print(f"Число в десятичной системе: {decimal_value}")
    else:
        print(Fore.RED + f"Ошибка: число {number_str} не может быть переведено в десятичную систему для основания {max_base}." + Style.RESET_ALL)

def show_menu():
    """Показывает меню с выбором задачи"""
    print(Style.BRIGHT + Fore.GREEN + "\n--- Решение задач 10-го задания ОГЭ по информатике ---" + Style.RESET_ALL)
    print(Style.BRIGHT + "Выберите тип задачи:")
    print("1 - Найти максимальное число среди чисел в разных системах счисления")
    print("2 - Найти число с минимальным количеством единиц в двоичной записи")
    print("3 - Найти число с минимальной суммой цифр в восьмеричной записи")
    print("4 - Найти наименьшее возможное основание системы счисления")
    print("5 - Найти наибольшее возможное основание системы счисления при ограничении")
    print("0 - Выход")

def main():
    """Основная функция, реализующая работу программы"""
    while True:
        show_menu()
        choice = input("\nВведите номер задачи: ").strip()
        if choice == '1':
            solve_task_1()
        elif choice == '2':
            solve_task_2()
        elif choice == '3':
            solve_task_3()
        elif choice == '4':
            solve_task_4()
        elif choice == '5':
            solve_task_5()
        elif choice == '0':
            print(Style.BRIGHT + Fore.GREEN + "Выход из программы." + Style.RESET_ALL)
            sys.exit()
        else:
            print(Fore.RED + "Неверный выбор. Пожалуйста, попробуйте снова." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
