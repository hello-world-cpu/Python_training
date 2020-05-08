#!/usr/bin/python3
D={}
for i in range(ord('a'), ord('z')+1):
	D[chr(i)]=i+1-ord('a')
while 1:
	try:
		letter=input("Enter a lowercase letter: ")
		if len(letter)!=1:
			raise ValueError
	except ValueError:
		print("Only one letter is expected.")
		continue
	try:
		if ord(letter) not in range(ord('a'), ord('z')+1):
			raise ValueError
			break
	except ValueError:
		print("This character is out of range.")
		continue
	print(D[letter])
	ask=input("y to continue, any key to stop: ")
	if ask!='y': quit()