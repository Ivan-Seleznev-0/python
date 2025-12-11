print("робот заехал в комнату")
print("сколько программистов в комнате?")
programmers = int(input("> "))
last_one = programmers % 10
last_two = programmers % 100
rooms = ("в комнате находится")
if 11 <= last_two <= 14:
    print(rooms, programmers, 'программистов')
else:
    if last_one == 1:
        print(rooms, programmers, 'программист')
    elif 2 <= last_one <= 4:
        print(rooms, programmers, 'программиста')
    else:
        print(rooms, programmers, 'программистов')