def capitalize(a):
	return a[0].upper()+a[1:]
try:
	inf=open('file3.txt')
	word=inf.read().split()
	b=""
	for i in word:
		r=capitalize(i)
		b=b+" "+r
	print(b)
	inf.close()
except IOError as io:
	print(io)