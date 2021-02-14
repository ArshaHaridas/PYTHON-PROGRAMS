try:
	inf=open('infile.txt','a')
	line=input("Enter a text:")
	while line:
		inf.write("\n"+line)
		line=input("Enter a text:")
	inf.close()
except IOError as io:
	print(io)