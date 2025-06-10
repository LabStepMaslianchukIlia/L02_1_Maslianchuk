import random
number = random.randint(0, 10)
win = False
print("Игра 'Угадай число' (от 0 до 10). У вас 3 попытки.")
for i in range(3):
    guess = int(input(f"Ваша {i+1} попытка: "))

    if guess == number:
        print("Поздравляем! Вы угадали!")
        win = True
        break
    elif guess < number:
        print("Неверно! Загаданное число больше.")
    else:
        print("Неверно! Загаданное число меньше.")
if not win:
    print(f"Вы проиграли. Число было: {number}")