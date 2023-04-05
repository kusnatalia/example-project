# trojkat
import math

a = 10
b = 20
c = 15
h = 12

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")

#prostokąt

a=10
b=15

obwod = 2*a+2*b
pole = a*b
print("Obwod prostokąta wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")


#koło

r=10

obwod = 2 * math.pi * r
pole = math.pi* r * 2
print("Obwod koła wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")

#romb
a=10
h=15

pole= a*h
obwod = 4*a
print("Obwod rombu wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")