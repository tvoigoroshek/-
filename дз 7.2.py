a=2,3,2,6
b=list(a)
def tpl_sort(b):
   for i in a:
      if i%1 != 0:
         print('Дробных чисел не должно быть!!!')
         break
   else:
      print(a)
tpl_sort(b)




