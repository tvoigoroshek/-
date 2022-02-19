####инкапсуляция
##class meow:
##    __name="Vasya"
##    __age=19
##    __sound="meeEEOOOW"
##ex=meow()
##print(ex.__sound)
##
####наследование
##
##class same:
##    paws=4
##    eyes=2
##    ears=2
##class dog(same):
##    sound="woof"
##class cat(same):
##    sound="meow"
##dg=dog()
##ct=cat()
##print(ct.paws)
##print(dg.paws)

##полиморфизм

class Cat:
    def make_sound(self):
        print("Meow")
        
class Dog:
    def make_sound(self):
        print("Bark")       
ct = Cat()
dg = Dog()

for animal in (ct, dg):
    animal.make_sound()

