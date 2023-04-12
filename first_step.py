# other files
from process_password_file import readFile
from first_step_rainbow_table import construction, sorting, output_table

# main()
def main():
	# read and process Passwords.txt file - process_password_file --> readFile
	passwords_list = readFile("Passwords.txt")
	
	# FIRST STEP #
	
	# number of passwords read is the length of the list
	number_of_passwords = len(passwords_list)
	
	# First Step - Q1
	print("-------------")
	print("First Step Q1")
	print("-------------")
	print(f"Number of passwords read: {number_of_passwords}\n")
	
	# First Step Q2
	print("-------------")
	print("First Step Q2")
	print("-------------")
	print("currently constructing rainbow table...\n")
	# construct rainbow table as a dictionary - first_step_rainbow_table.py --> construction
	rainbow_table = construction(passwords_list)
	
	print("Rainbow table constructed!\n")
	
	# First Step Q3
	print("-------------")
	print("First Step Q3")
	print("-------------")
	print("sorting rainbow table...\n")
	# sorting rainbow table by its hash value - first_step_rainbow_table.py --> sorting
	sorted_rainbow = sorting(rainbow_table)
	print("Sorting complete!\n")
	
	# First Step Q4
	print("-------------")
	print("First Step Q4")
	print("-------------")
	print("writing rainbow table to Rainbow.txt...\n")
	# output the sorted rainbow table into Rainbow.txt - first_step_rainbow_table.py --> output_table
	output_table(sorted_rainbow)
	print("Finished writing to Rainbow.txt!\n")
	# number of lines in rainbow table
	print(f"Number of lines in rainbow table: {len(sorted_rainbow)}")

	# END OF FIRST STEP #
	
# driver of the program
if __name__ == "__main__":
	main()
