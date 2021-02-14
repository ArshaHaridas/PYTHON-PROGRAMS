try:
	inf = open("file1.txt", "r")
	lines = inf.readlines()
	inf.close()
	outf = open("file2.txt", "w")
	for line in lines:
		if not (line.startswith('#')):
			outf.write(line)

	outf.close()
except IOError as io:
	print(io)