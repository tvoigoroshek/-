lst=[1,2,3,4,5,6,7,8]
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)
change(lst)
