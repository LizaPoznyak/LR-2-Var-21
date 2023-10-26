# Написать функцию для определения всех чисел, на которые без остатка делится указанное число.

def func(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    print("Все делители числа :\n", divisors)
    pass


while True:
    try:
        digit = int(input("Введите число : "))
        if digit > 0:
            func(digit)
            break
        else:
            print("Число равно нулю!")
    except Exception:
        print("Некорректный ввод!")
