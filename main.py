import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать его!")

    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1

            if guess < secret_number:
                print("Слишком мало. Попробуй еще раз.")
            elif guess > secret_number:
                print("Слишком много. Попробуй еще раз.")
            else:
                print(f"Поздравляю. Ты угадал число {secret_number} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, вводите только целые числа.")

# Запуск игры
guess_the_number()
