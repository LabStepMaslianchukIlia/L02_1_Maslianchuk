# 7. Функции - mydef.py (5%)
# Напишите функцию, которая принимает два числа и возвращает их сумму.
# Напишите функцию, которая проверяет, является ли число простым.
# Напишите функцию, которая принимает список чисел и возвращает их среднее значение.

# -----------------------------_1_-----------------------------

def sum_two_numbers(a, b):
    return a + b
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
result = sum_two_numbers(num1, num2)
print("Сумма:", result)

# -----------------------------_2_-----------------------------

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
number = int(input("Введите число для проверки на простоту: "))
if is_prime(number):
    print(f"{number} — простое число.")
else:
    print(f"{number} — не простое число.")
    
# -----------------------------_3_-----------------------------

def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
numbers_input = input("Введите числа через пробел: ")
number_list = list(map(float, numbers_input.split()))
avg = average(number_list)
print("Среднее значение:", avg)