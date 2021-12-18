def qwer():
    a= input(": ")
    b = input(": ")    
meow = False
while not meow:
    if type(a)==None or type(b)==None :
        print(a+b)
    elif type(a)==str or type(b)==str :
        l=[a,b]
        print(tuple(l))
    else:
        print(a+b)
        continue 
qwer()
