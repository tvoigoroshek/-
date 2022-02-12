##class ipad:
##    def photo(self):
##        print('You can take pictures,if you want')
##    def app(self):
##        print('You can download apps')
##    def calculate(self):
##        print(5+9)
##    def video(self):
##        print('You can take video')
##    def call(self):
##        print('You can talk to someone,who is far from you')
##        
##class iphone(ipad):
##    a="smth"
##func= iphone()
##print(func.photo)
people = int(input("Сколько вас? "))
meat = input("Какое мясо жарим(свинина, говядина, курица, баранина, растительное мясо? ")
hungry = int(input("Насколько вы голодные(%)? "))
kaif = int(input("Как долго планируем балдеть(1. Мы быстро — по полшашлычинки и домой! 2. Нормально посидим! И так редко собираемся. 3. Пока мангал не развалится!) ? "))
a = people*0.5
class Meat:
    def __init__(self,people,meat,hungry,kaif):
        self.people = people
        self.meat = meat
        self.hungry = hungry
        self.kaif = kaif
    def PRINT(self):
        if meat == 'свинина':
            print("Ваш рецепт шашлычного балдежа: ", a, 'кг свинины')
        elif meat == 'говядина':
            print("Ваш рецепт шашлычного балдежа: ", a, 'кг говядины')
        elif meat == 'баранина':
            print("Ваш рецепт шашлычного балдежа: ", a, 'кг баранины')
        elif meat == 'курица':
            print("Ваш рецепт шашлычного балдежа: ", a, 'кг курицы')
        elif meat == 'растительное мясо':
            print("Ваш рецепт шашлычного балдежа: ", a, 'кг растительного мяса')
meat = Meat(people,meat, hungry, kaif)
meat.PRINT()

