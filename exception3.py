class CheckEx (Exception):
	pass
try:
	name=input("enter a username:")
	psw=input("enter password:")
	a="arsha@gmail.com"
	b="arsha123"
	if name==a and psw==b:
		print("Valid Login")
	else:
		raise CheckEx("Invalid Login")
except CheckEx as e:
	print(e)