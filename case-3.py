import random

def play_game():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. У тебя есть 10 попыток, чтобы его угадать.")
    
    secret_number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            guess = int(input(f"Осталось попыток: {attempts}. Введи свое предположение: "))
            
            if guess < 1 or guess > 100:
                print("Ошибка: Ввод должен быть целым числом от 1 до 100.")
                continue
            
            if guess < secret_number:
                print("Слишком маленькое число!")
            elif guess > secret_number:
                print("Слишком большое число!")
            else:
                print(f"Поздравляю! Ты угадал число {secret_number}!")
                break
            
            attempts -= 1
            
        except ValueError:
            print("Ошибка: Пожалуйста, введи корректное целое число.")

    if attempts == 0:
        print(f"Увы, ты не угадал число. Оно было {secret_number}.")
    
def main():
    while True:
        play_game()
        repeat = input("Хотите сыграть снова? (да/нет): ").strip().lower()
        if repeat != 'да':
            print("Спасибо за игру! До встречи!")
            break

if name == "main":
    main()