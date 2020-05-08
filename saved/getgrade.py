#!/usr/bin/python3

def getgrade():
	while 1:
		n=input("Enter an integer in range [0, 100]:\n")
		try:
			m=int(n)
		except ValueError:
			print("Incorrect data type")
			continue
		try:
			if m!=float(n):	#check if the user entered a decimal number which isn't an integer
				raise TypeError
		except TypeError:
			print("You entered a float with a non-zero fractional part")
			continue
		try:
			if m not in range(0, 101):
				raise RuntimeError
			break
		except RuntimeError:
			print("The entered integer is not in range [0, 100]")
			continue
	if m in range(75, 101):
		q="first"
	elif m in range(50, 75):
		q="second"
	elif m in range(25, 49):
		q="third"
	else:
		q="fourth"
	print(n, "is in the", q, "quartile.")

getgrade()