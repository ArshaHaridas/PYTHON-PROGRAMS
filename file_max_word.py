try:
	inf = open("output.txt", "r")
	words=inf.read().split()
	max_len = len(max(words, key=len))
	for word in words:
		if len(word)==max_len:
			print("Longest word is:",word)
	inf.close()
except IOError as io:
	print(io)