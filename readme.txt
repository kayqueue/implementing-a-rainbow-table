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
