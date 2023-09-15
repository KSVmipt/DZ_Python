a = input()
numbers = a.split(' ')
for i in range(1, len(numbers)+1):
    i = str(i)
    if i in numbers[1:]:
        pass
    else:
        print("Потеряннная карта:", i)