x = ""
while(x != "stop"):
	x = raw_input("")
	try:
		z = float(x)
		print z , pow(z , 3)
	except ValueError:
		if x != "stop":
			print "STRING!"