line = input("Введи числа(через пробел): ")
chisla = line.split(' ')
summ = 1
for i in chisla:
    summ = summ * int(i)
geom = summ**(1/len(chisla))
print("Среднее геометрическое - ", geom)
input()