import datetime 
 
def date(): 
    now = datetime.datetime.now() 
    a = now.year 
    b = int(input("Введите ваш возраст: ")) 
    c = input("Введите было ли у вас день рождения в этом году: ") 
    d = a - b 
    if c == 'Да': 
        print("Год вашего рождения: ", d) 
    elif c == 'Нет': 
        print("Год вашего рождения: ", d - 1) 
    else: 
        print("Error") 
date()
