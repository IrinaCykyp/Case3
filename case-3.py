import random

def play_game():
    print("����� ���������� � ���� '������ �����'!")
    print("� ������� ����� �� 1 �� 100. � ���� ���� 10 �������, ����� ��� �������.")
    
    secret_number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            guess = int(input(f"�������� �������: {attempts}. ����� ���� �������������: "))
            
            if guess < 1 or guess > 100:
                print("������: ���� ������ ���� ����� ������ �� 1 �� 100.")
                continue
            
            if guess < secret_number:
                print("������� ��������� �����!")
            elif guess > secret_number:
                print("������� ������� �����!")
            else:
                print(f"����������! �� ������ ����� {secret_number}!")
                break
            
            attempts -= 1
            
        except ValueError:
            print("������: ����������, ����� ���������� ����� �����.")

    if attempts == 0:
        print(f"���, �� �� ������ �����. ��� ���� {secret_number}.")
    
def main():
    while True:
        play_game()
        repeat = input("������ ������� �����? (��/���): ").strip().lower()
        if repeat != '��':
            print("������� �� ����! �� �������!")
            break

if name == "main":
    main()