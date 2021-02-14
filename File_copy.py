inf=False
outf=False
try:
	inf=open('infile.txt')
	outf=open('outfile.txt','w')
	line=inf.read()
	while line:
		outf.write(line)
		inf=False
		inf=open('outfile.txt')
		line=inf.readline()
	print(line)
except IOError as io:
	print(io)
finally:
	if inf:inf.close()
	if outf:outf.close()
		
