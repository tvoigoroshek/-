a=int(input("Введите число: "))
if a > 1:
    for i in range(2, int(a/2)+1):
         if (a % i) == 0:
            print("Не четное")
            break
    else:
        print("Четное")

