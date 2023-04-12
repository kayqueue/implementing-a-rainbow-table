# Goal 1: Given a password file "Passwords.txt", construct a Rainbow Table.
---------------------------------------------------------------------------
1. for each un-processed password from "Passwords.txt", apply a hash function
2. apply reduction function to the hash value obtained
3. repeat step 2 four more times
4. store original word processed in step 1 and the final hash as an entry in the rainbow table

# Goal 2: Finding pre-images from a given hash value
----------------------------------------------------
1. user inputs a hash value
2. program attempts to find the pre-image of the requested hash value against the constructed rainbow table in Goal 1
3. program runs until a pre-image is found, or until it performs the reduction + hash enough times that it is clear that something is wrong

# Compilation Instructions
---------------------------
- to run the program
1. open up the terminal and cd into Part Two directory
2. to generate Rainbow table, run the following command in the terminal: python first_step.py
3. to find pre-image based on requested hash, run the following command in the terminal: python second_step.py

# Reduction function sequence
------------------------------
# FORMULA
reduction_value = decimal % number of passwords

# pre-condition: before engaging in the reduction function sequence, a hash would have already been generated from the password the program is currently processing.

BEGIN REDUCTION SEQUENCE
Step 1: convert the hash to an integer
- i used the following command to convert -> int(hex_of_hash, 16)

Step 2: get reduction value
- reduction_value = int(hex_of_hash, 16) % number of passwords

Step 3: obtain the respective password
- new password to be processed = password_list[reduction_value]

example:
password_list = ["abc", "123", "def", "456", "ghi", "789"]

# processing the first password in the list at position 0 - "abc" using md5 algorithm
hex_of_hash = hashlib.md5(password_list[0].encode()).hexdigest()

# convert hash to integer
decimal = int(hex_of_hash, 16)

# get reduction value
reduction_value = decimal % len(password_list)

# obtain the respective password for further processing
new_password_to_be_processed = password_list[reduction_value]

# the above example will be in a loop until EITHER 5 reductions have been performed
# OR the new_password_to_be_processed has already been processed, whichever comes first
