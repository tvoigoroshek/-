num1={1,2,3,4,5}
num2={8,5,9,7,0}
num3={11,23,56,74}
num4={45,67,33,98}
a=int(input("Введите число:"))
b=int(input("Введите число:"))
if b==0:
    print("Error")
else:
    c=a/b
    print(c)
    if c > 10:
        d=set()
        d.update(num1,num2)
        d.add(10)
        print(d)
    if c < 10:
        f=set()
        f.update(num1,num2,num3,num4)
        print(f)
    if c==10:
        r=set()
        r.update(num1,num2,num3,num4)
        print(r.clear())

 
