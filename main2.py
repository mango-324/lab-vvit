stroka = input()
test = stroka.replace(" ", "").replace("-", "").replace(".", "")
if test.isdigit():
    a, b, c = map(float, stroka.split())
    if a == 0:
        if b != 0:
            print(-c / b)
        if b == 0:
            print(c)
    else:
        D = b ** 2 - (4 * a * c)
        if D > 0 or D < 0:
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            print(x1)
            print(x2)
        elif D == 0:
            x = (-b) / (2 * a)
            print(x)
else:
    print("Впишите числа")