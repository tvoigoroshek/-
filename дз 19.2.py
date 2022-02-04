class cact:
    def __init__(self,name,age,spike,length):
        self.name = name
        self.age = age
        self.spike = spike
        self.length = length
pr = cact('Miron',2,43,15)
print(pr.name)
print(pr.length+pr.spike)
print(pr.length-pr.age)
