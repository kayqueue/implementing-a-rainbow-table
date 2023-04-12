# other files
from second_step_request_hash import request_hash
from second_step_find_password import read_rainbow_table, pre_image

# main()
def main():
	# SECOND STEP #
	
	# request hash from user - second_step_request_hash --> request_hash
	requested_hash = request_hash()
	
	# Second Step - Q1
	print("-------------")
	print("Second Step Q1")
	print("-------------")
	print("checking whether the requested hash is in the rainbow table...\n")
	
	# construct the rainbow table as a dictionary - second_step_find_password --> read_rainbow_table
	rainbow_table = read_rainbow_table("Rainbow.txt")
	
	# invoke method to find whether the requested hash is in the rainbow table
	if requested_hash in rainbow_table.values():
		print("Ans: The requested hash is in the rainbow table.\n")
	else:
		print("Ans: The requested hash is NOT in the rainbow table.\n")
	
	# Second Step Q2 - Q4
	print("-------------------")
	print("Second Step Q2 - Q4")
	print("-------------------")
	print("looking for pre-image of the requested hash...")
	
	# output the pre-image from the requested hash - second_step_find_password --> pre_image
	pre_image(requested_hash, rainbow_table)

	# END OF SECOND STEP #
	
# driver of the program
if __name__ == "__main__":
	main()
