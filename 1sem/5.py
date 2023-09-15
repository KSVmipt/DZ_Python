chislo = input("Введи число:")
osn = int(input('Введи его основание:'))
sist = int(input('Введи в какую систему перевести:'))
chislo_des = int(chislo, osn)

def convert_to(number, baza, upper=True):
    cifri = '0123456789abcdefghijklmnopqrstuvwxyz'
    if baza > len(cifri): return None
    rez = ''
    while number > 0:
        rez = cifri[number % baza] + rez
        number //= baza
    return rez.upper() if upper else rez
print('Число в', str(sist) + '(р)ичной', 'системе счисления:', convert_to(chislo_des, sist))

    
     
    

