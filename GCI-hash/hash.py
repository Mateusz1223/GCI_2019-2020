import hashlib

class textColors:
	ERROR = '\033[1;31;48m'
	SUCCES = '\033[1;32;48m'

	END = '\033[1;37;48m'

def hash():
	choice = input("1.md5\n2.sha1\n3.sha224\n4.sha256\n5.sha384\n6.sha512\nType number: ")

	if choice == '1':
		hashFunc = hashlib.md5
	elif choice == '2':
		hashFunc = hashlib.sha1
	elif choice == '3':
		hashFunc = hashlib.sha224
	elif choice == '4':
		hashFunc = hashlib.sha256
	elif choice == '5':
		hashFunc = hashlib.sha384
	elif choice == '6':
		hashFunc = hashlib.sha512
	else:
		print(textColors.ERROR+"Incorrect input!\n"+textColors.END)
		main()

	string = input('Enter String to hash: ')
	hash_object = hashFunc(string.encode())
	print(textColors.SUCCES+hash_object.hexdigest()+'\n'+textColors.END)
	main()

def crack():
	hashString = input("Enter the hash: ")
	hashType = ''

	hashLength = len(hashString)
	if hashLength == 32:
		hashFunc = hashlib.md5
		hashType = 'md5'
	elif hashLength == 40:
		hashFunc = hashlib.sha1
		hashType = 'sh1'
	elif hashLength == 56:
		hashFunc = hashlib.sha224
		hashType = 'sha224'
	elif hashLength == 64:
		hashFunc = hashlib.sha256
		hashType = 'sha256'
	elif hashLength == 96:
		hashFunc = hashlib.sha384
		hashType = 'sha384'
	elif hashLength == 128:
		hashFunc = hashlib.sha512
		hashType = 'sha512'
	else:
		print(textColors.ERROR+"Incorrect hash!\n"+textColors.END)
		main()

	passListName = input("Enter password list file name: ")

	try:
		passList = open(passListName, 'r')
	except:
		print(textColors.ERROR+"File "+passListName+" doesn't exists!\n"+textColors.END)
		main()

	while(True):
		password = passList.readline()
		if password[len(password)-1] == '\n':
			password = password[:-1]

		if password == "":
			break
		else:
			passHash = hashFunc(password.encode())
			if hashString == passHash.hexdigest():
				print(textColors.SUCCES+'Succes! Found: ' + hashString + ' = "' + password + '" ('+hashType+')\n'+textColors.END)
				passList.close()
				main()

	print(textColors.ERROR+"Failure. Hash hasn't been found in "+passListName+'\n'+textColors.END)
	main()


def main():
	print("1. hash\n2. crack hash")
	choice = input("Type number: ")

	if choice == '1':
		hash()
	elif choice == '2':
		crack()
	else:
		print(textColors.ERROR+"Incorrect input!\n"+textColors.END)
		main()

if __name__ == "__main__":
	main()

	#hStr = "2b5801d08603c0d5f4db58b71dc5ff22e1e3d3b88ac43dcc4468d1cbbaf3c4631c066a848818c4ed52fb329ec8a9ea77aa470d397040f2d938d1a9c8da6fa96c"
	#real = hashlib.sha512(b"de")

	#if hStr == real.hexdigest():
	#	print("yes")
	#else:
	#	print("no")