
#vigade otsing/moodle 

import math 


print("Ruudu karakteristikud")

a=float(input('Sisesta ruudu külje pikkus => '))
S=a**2
print("Ruudu pindala",round(S,1))
P=4*a
print("Ruudu ümbermõõt",round(P,1))
di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()

print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c

print("Ristküliku pindala:",round(S,1))
P=2* (b+c)
print("Ristküliku ümbermõõt",round(P,1))
di = math.sqrt(b**2 + c**2)
print("Ristküliku diagonaal:", round(di,1))
print()

print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiuse pikkus => "))
d=2*r
print("Ringi läbimõõt:",round(d,1))
S=math.pi * r**2
print("Ringi pindala:", round(S,2))
C=2 * math.pi * r
print("Ringjoone pikkus:", round(C,2))
