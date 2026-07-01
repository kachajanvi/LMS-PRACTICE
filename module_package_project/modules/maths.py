import math

def factorial():
    print("Factorial:", math.factorial(int(input("Number : "))))

def interest():
    p = float(input("Principal: "))
    r = float(input("Rate: "))
    t = float(input("Time: "))
    print("SI:", p*r*t/100)
    print("CI:", p*((1+r/100)**t)-p)

def trig():
    a = math.radians(float(input("Angle: ")))
    print("Sin:", math.sin(a))
    print("Cos:", math.cos(a))
    print("Tan:", math.tan(a))

def geometry():
    c = input("1.Circle 2.Rectangle 3.Triangle: ")
    if c == "1":
        r = float(input("Radius: "))
        print("Area:", math.pi*r*r)
        print("Perimeter:", 2*math.pi*r)

    elif c == "2":
        L = float(input("Length: "))
        W = float(input("Width: "))
        print("Area:", L*W)
        print("Perimeter :", 2*(L+W))

    elif c == "3":
        b = float(input("Base: "))
        h = float(input("Height: "))
        print("Area:", 0.5*b*h)

    else:
        print("Invalid Choice")