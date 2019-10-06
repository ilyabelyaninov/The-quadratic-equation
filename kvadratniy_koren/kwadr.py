a = float(input("Введите a "))
b = float(input("Введите b "))
c = float(input("Введите c "))
discr = (b ** 2) - (4 * a * c)
if discr > 0:
    x1 = (-b + discr ** 0.5)/2 * a
    x2 = (-b - discr ** 0.5)/2 * a
    print ("x1 = ", x1)
    print("x2 = ", x2)
elif discr == 0:
    x = (-b) / 2 * a
    print("x = ", x)
else:
    print ("Корней нет")
