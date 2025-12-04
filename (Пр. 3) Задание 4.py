Pi = 3.14
rooms = "\n прямоугольник - 1\n треугольник- 2\n круг- 3"
print(rooms)
print("Введите тип комнаты: ")
type_room = input()
if type_room == "1":
    print("введи длину и ширину")
    a = int(input("длина -"))
    b = int(input('ширина -'))
    formula = a * b
    print('ответ -', formula)
elif type_room == "2":
    print('треугольная комната? эээм, окей')
    print('введи длины сторон')
    a =int(input('длина стороны - '))
    b =int(input('длина стороны - '))
    c =int(input('длина стороны - '))
    P = (a + b + c) / 2
    formula = (P * (P - a) * (P - b) * (P - c)) ** 0.5
    print('ответ - ', formula)
elif type_room == "3":
    print('КРУГЛАЯ?!?!???! КАКИМ ОБРАЗОМ, а хотя мне как то по барабану')
    print("Введи радиус круга")
    r = int(input("радиус круга - "))
    formula = (Pi * r * r)
    print('ответ - ', formula)
else:
    print('напиши цифру, идиотина тупорылая')