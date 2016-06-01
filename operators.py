import fractions
import math
#operators
a = 12
b = 6
c = 5
#a // c rounds of the quotient
print("\na // b =", a // b, "\na // c = ", a//c)
print("pow(a, b) =", a**b)
#fractions

print(fractions.Fraction(1, 3))
#Get reduced automatically
print(fractions.Fraction(2, 6))
a = fractions.Fraction(1, 3) + fractions.Fraction(4, 7)
print(a)

#Trigonometry
print(math.pi)
#Not 0 since Python does not have infinite precision
print(math.sin(math.pi))
print(math.cos(math.pi))
print(math.pi*2**2)


