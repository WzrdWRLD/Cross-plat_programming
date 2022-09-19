print("Hello!")
try:
    a = float(input('Введите a: '))
    b = float(input('Введите b: '))
    x = float(input('Введите x: '))
    try:
        if (x < 7):
            y = (2 * a * b * x)/pow((a + b), 2)
        else:
            y = x*(pow((a), 2) + 4*b)
        print('y =', y)
    except:
        print("Нет решения!")
except:
    print("Неверные входные данные")