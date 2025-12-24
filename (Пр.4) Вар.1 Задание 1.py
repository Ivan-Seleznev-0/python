chislo = input("введи цифарки: ")
if chislo[0] == "-":
    chto = chislo[1:]
    print(chto)
elif chislo == "0":
    print("1")
else:
    print(chislo)