class plus:
    def plus1(n,s):
        print(n+s)
class minus:
    def minus1(n,s):
        print(n-s)
class umnozh:
    def umnozh1(n,s):
        print(n*s)
class delit:
    def umnozh1(n,s):
        print(n/s)
class kalkulyatop(plus,minus,umnozh,delit):
     def __init__(self, n, s):
        self.n=n
        self.s=s
  
p1 = kalkulyatop(4,3)
print(p1.minus1)
print(p1.plus1)
print(p1.umnozh1)
