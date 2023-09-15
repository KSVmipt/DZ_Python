with open('input.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    chisla = lines[0].split(' ')
    oper = lines[1]
    zero = 0
    one = 1
    summ = 0
    minus = int(chisla[0])
    if oper == "+":
        for i in chisla:
            summ = int(i) + summ
            with open('output.txt','w') as output:
                output.write(str(summ))
    if oper == "-":
        for i in chisla[1:]:
            minus = minus - int(i)
            with open('output.txt','w') as output:
                output.write(str(minus))
    if oper == "*":
        for i in chisla:
            one = one*int(i)
        with open('output.txt','w') as output:
                output.write(str(one))
    
            
            
