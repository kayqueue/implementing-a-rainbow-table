# imports
from process_password_file import readFile

import hashlib

# read and process Passwords.txt file - process_password_file.py --> readFile
# global variable
passwords_list = readFile("Passwords.txt")

# read the contents of Rainbow.txt
def read_rainbow_table(filename):
	rainbow_table = {}

	with open("Rainbow.txt", "r") as fin:
		lines = fin.readlines()
		
		for line in lines:
			split_line = line.strip().split(": ")
			key = split_line[0]
			value = split_line[1]
			rainbow_table.update({key: value})
			
	return rainbow_table
	
# finding preimage
def pre_image(hash, rainbow_table):
	
	# if hash in rainbow table
	if hash in rainbow_table.values():
		inside(hash, hash, rainbow_table)
	else: # if hash is not in rainbow table
		outside(hash, hash, rainbow_table, 0)

# reduction function
def reduction_function(hash):
	# reduce hash
	decimal = int(hash, 16)
	reduction_value = decimal % len(passwords_list)
	pre_image = passwords_list[reduction_value]

	return pre_image

# if hash in rainbow table - recursive function
def inside(hash, current_hash, rainbow_table):
	try:
		print(f"{current_hash} is in the rainbow table...")
		
		# get preimage of hash in the rainbow table
		pre_image = list(rainbow_table.keys())[list(rainbow_table.values()).index(current_hash)]
		
		print(f"pre_image: {pre_image}\n")
		
		# hash the pre-image
		hash_pre = hashlib.md5(pre_image.encode()).hexdigest()		
		
		# compare hash with original
		print(f"{hash_pre} ? {hash}\n")
		
		# if equals - pre image found
		if hash_pre == hash:
			print(f"Pre-image: {pre_image} found!")
			return

		# if hash is inside rainbow table
		if hash_pre in rainbow_table.values():
			# print(f"calling inside() function...\n")
			inside(hash, hash_pre, rainbow_table)
		else: # if hash in not inside rainbow table
			# print(f"calling outside() function...\n")
			outside(hash, hash_pre, rainbow_table, 0)	
	except:
		print("The requested hash cannot be found - recursion depth")
		
# if hash is not in rainbow table - recursive function
def outside(hash, current_hash, rainbow_table, iteration):
	try:
		print(f"reduction count: {iteration + 1}\n")

		# apply reduction to get preimage of the next password
		pre_image = reduction_function(current_hash)
		
		print(f"pre_image: {pre_image}\n")
		
		# hash the pre-image
		hash_pre = hashlib.md5(pre_image.encode()).hexdigest()		
		
		# compare hash with original
		print(f"{hash_pre} ? {hash}\n")
		
		# if equals - pre image found
		if hash_pre == hash:
			print(f"Pre-image: {pre_image} found!")
			return

		# if hash is inside rainbow table
		if hash_pre in rainbow_table.values():
			print(f"calling inside() function...\n")
			inside(hash, hash_pre, rainbow_table)
		elif iteration < 4: # if hash is not inside rainbow table
			print(f"calling outside() function...\n")
			outside(hash, hash_pre, rainbow_table, iteration + 1)
		else: # cannot be found after 5 reductions
			print(f"The requested hash cannot be found after {iteration + 1} reductions")
	except:
		print("The requested hash cannot be found - recursion depth")
