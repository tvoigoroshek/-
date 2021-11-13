v = '''Если вам нужно найти площадь треугольника-нажмите 1
Если вам нужно найти длинну окружности-нажмите 2
Если вам нужно найти периметр квадрата-нажмите 3'''
print(v)
g=int(input("Что вам нужно посчитать?: "))
if g==1:
    from md81 import area_triangle

if g==2:
    from md82 import circumference

if g==3:
    from md83 import perimeter_square

