def convert_to(number, baza, upper=True):
    cifri = '0123456789abcdefghijklmnopqrstuvwxyz'
    if baza > len(cifri): return None
    rez = ''
    while number > 0:
        rez = cifri[number % baza] + rez
        number //= baza
    return rez.upper() if upper else rez

def convert_to_des(m, n):
    z = int(m, n)
    return z




with open('input.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    chisla = lines[0].split(' ')
    oper = lines[1]
    chisla_des = []
    zero = 0
    one = 1
    summ = 0
    minus = int(chisla[0], int(lines[2]))
    for i in chisla:
        des = convert_to_des(i, int(lines[2]))
        chisla_des.append(des)
    if oper == "+\n":
        for i in chisla_des:
            summ = i + summ
            with open('output.txt','w') as output:
                output.write(str(convert_to(summ,int(lines[2]))))
    if oper == "-\n":
        for i in chisla_des[1:]:
            minus = minus - i
            with open('output.txt','w') as output:
                output.write(str(convert_to(minus,int(lines[2]))))
    if oper == "*\n":
        for i in chisla_des:
            one = one*i
        with open('output.txt','w') as output:
                output.write(str(convert_to(one,int(lines[2]))))