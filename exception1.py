'''Write a program to demonstrate ZeroDivisionError and ValueError'''

try:
	n1=int(input("enter 1st number:"))
	n2=int(input("enter 2nd number:"))
	print("quotient=",(n1/n2))
except(ZeroDivisionError,ValueError) as e:
	print(e)
else:
	print("Divided Successfully")
finally:
	print("Finally block")
