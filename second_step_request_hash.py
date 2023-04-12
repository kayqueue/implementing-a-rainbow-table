# request hash value from user
def request_hash():
	while True:
		user_input = input("Enter a hash: ")

		# check for validity of input string
		if not validate_string(user_input):
			print("Please enter a valid hash!")
			continue
		else:
			return user_input
			break

# validate the hash string provided by the user
def validate_string(s):
	# check for hash length == 32 (md5 hash output length)
	if len(s) != 32:
		return False

	# check whether user_input is in hexadecimal
	for c in s:
		# not hexadecimal
		if ((c < '0' or c > '9') and (c < 'a' or c > 'f')):
			return False

	# return True if string passes both checks
	return True

