from graphics import Rectangle as r
print("\nRECTANGLE\n")
l=float(input("enter length of rectangle:"))
b=float(input("enter breadth of rectangle:"))
print("Area=",r.Rectarea(l,b))
print("Perimete=",r.Rectperi(l,b))


from graphics import Circle as c
print("\nCIRCLE\n")
r=float(input("enter radius:"))
print("Area=",c.Circlearea(r))
print("Perimeter=",c.Circleperi(r))

from graphics.dgraphics import cuboid as cu
print("\nCUBOID\n")
a=float(input("enter length:"))
b=float(input("enter Width:"))
c=float(input("enter Height:"))
print("Surface Area=",cu.Cuboidsa(a,b,c))
print("Volume=",cu.Cuboidvolume(a,b,c))

from graphics.dgraphics.sphere import *
print("\nSPHERE\n")
s=float(input("enter the radius:"))
print("Surface Area=",Spherearea(s))
print("Volume=",Spherevolume(s))