import hashlib # for hashing
import json # for converting dictionary to string, to write to file

def construction(passwords_list):
	# rainbow table as a dictionary
	rainbow_table = {}

	# a list to keep track of processed passwords
	processed_passwords = []

	# process each password
	for each in passwords_list:
		# PASSWORD PROCESSED
		if each in processed_passwords:
			continue
		
		# PASSWORD NOT PROCESSED YET
		# track the iteration of reduction
		iteration = 0
		current_password = each
		
		# maximum of 5 reductions - 1 reduction plus 4 repeats
		while iteration < 6:
			# add to processed_passwords list
			processed_passwords.append(current_password)
			
			# hash the password
			current_hash = hashlib.md5(current_password.encode()).hexdigest()
			
			
			# perform reduction on the current hash
			pre_image = reduction_function(current_hash, passwords_list)
			
			# the password has already been processed
			# this is to prevent collision
			if pre_image in processed_passwords or iteration == 5:
				rainbow_table.update({each: current_hash})
				break
			else:
				# update the current_password and increment iteration
				current_password = pre_image
				iteration += 1
				
	return rainbow_table
	
# reduction function
def reduction_function(hash, passwords_list):
	# reduce hash
	decimal = int(hash, 16)
	reduction_value = (decimal % len(passwords_list))
	pre_image = passwords_list[reduction_value]

	return pre_image


# sorting the rainbow table by hash values
def sorting(rainbow_table):
	# sorted() function returns a list, so have to convert it back to a dictionary
	sorted_rainbow = dict(sorted(rainbow_table.items(), key = lambda x:x[1]))
	
	return sorted_rainbow


# output rainbow table to a txt file
def output_table(rainbow_table):
	with open("Rainbow.txt", "w") as fout:
		for key, value in rainbow_table.items():
			fout.write(f"{key}: {value}\n")
