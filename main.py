import math
a=float(input("Podaj wartość liczby a "))
b=float(input("Podaj wartość liczby b "))
c=float(input("Podaj wartość liczby c "))
x=[]
def RowKwa():
    try:
        delta=pow(b,2)-4*a*c
        x1=(-b+math.sqrt(delta))/2*a
        x2=(-b-math.sqrt(delta))/2*a
        x.append(x1)
        x.append(x2)
    except ValueError:
        print("Nie można kontynuować, ponieważ delta wyszła ujemna")

RowKwa()
if len(x)==0:
    pass
else:
    print("Wynik wynosi:" )
    print("x=" , x)
