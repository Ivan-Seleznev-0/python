print('Сколько Аня спит?')
hours = int(input("> "))
if hours < 8:
    print('недосып')
elif hours > 11:
    print('пересып')
elif hours >= 8 and hours <=11:
    print('это нормально')