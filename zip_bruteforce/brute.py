import subprocess
import os
import sys

class textColors:
	ERROR = '\033[1;31;48m'
	SUCCES = '\033[1;32;48m'

	END = '\033[1;37;48m'

def bruteforce(passListName, zipName):
	try:
		passList = open(passListName, 'r')
	except:
		print(textColors.ERROR+'File: "'+passListName+'" cannot be opened!'+textColors.END)
		exit()

	while(True):
		password = passList.readline()

		if password == "":
			print(textColors.ERROR+"Password hasn't been found in "+passListName+textColors.END)
			exit()

		if password[len(password)-1] == '\n':
			password = password[:-1]

		cmd = "unzip -P "+password+" "+zipName
		returnCode = subprocess.call(cmd, shell=True)
		if returnCode == 1:
			continue
		if returnCode == 9:
			print(textColors.ERROR+"Archive "+zipName+" cannot bo open!"+textColors.END)
			exit()
		if returnCode == 0:
			print(textColors.SUCCES+'Succes! Zip archive has been unziped. The password is "'+password+'"'+textColors.END)
			exit()

def main():
	try:
		passListName = sys.argv[1]
	except:
		print(textColors.ERROR+"Incorrect input!")
		print("Usage: python3 brute.py password_list FILE[.zip]"+textColors.END)
		exit()

	try:
		zipName = sys.argv[2]
	except:
		print(textColors.ERROR+"Incorrect input!")
		print("Usage: python3 brute.py password_list zip_folder"+textColors.END)
		exit()

	bruteforce(passListName, zipName)


if __name__ == "__main__":
	main()