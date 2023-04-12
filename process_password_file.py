# read and process file
def readFile(filename):
	# list to store passwords
	password_list = []

	# read password file
	with open(filename, "r") as fin:
		# read every line
		lines = fin.readlines()
		
		for line in lines:
			password_list.append(line.strip())
	# end of password file processing
	
	return password_list
	
