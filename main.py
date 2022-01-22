import math

def RowKwa(a,b,c):
    x = []
    delta=pow(b,2)-4*a*c
    x1=(-b+math.sqrt(delta))/2*a
    x2=(-b-math.sqrt(delta))/2*a
    x.append(x1)
    x.append(x2)
    if len(x) != 0:
        print("Wynik wynosi:")
        print("x1=", x[0])
        print("x2=", x[1])
        return True




