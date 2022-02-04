from itertools import *
count=1
for i in cycle("Программирование"):
    if count>8:
        break
    print(i)
    count+=1 
