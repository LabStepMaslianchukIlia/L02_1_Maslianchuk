
text = input("Введите выражение (например: 2 + 2): ")
parts = text.split()
if len(parts) != 3:
    print("Ошибка: Неверный формат. Используйте: ЧИСЛО ОПЕРАЦИЯ ЧИСЛО")
else:
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])

    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b == 0:
            print("Ошибка: Деление на ноль!")
        else:
            print("Результат:", a / b)
    else:
        print("Неизвестная операция")