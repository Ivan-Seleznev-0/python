first_num = int(input("введи первое число: "))
second_num = int(input("введи второе число: "))
if first_num % 3 == 0 and second_num % 3 == 0:
    print(True)
elif first_num % 3 == 0 or second_num % 3 == 0:
    print("одно число только делится")
else:
    print(False)