d = {1:'one' , 2: 'two', 3: 'three'}
d.items()
def dict_items():
    for key, value in d.items():
        d1={value:key}
        print(d1)
dict_items()

