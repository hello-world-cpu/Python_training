#!/usr/bin/python3
#this script copy the content of a file to another file, with the line nimber in the margin, followed by the proper number of spaces
#to keep the text aligned. Max number of lines = 9999 to keep it aligned (change 3 to higher integer at line 20 to extend it)
import math

while 1:
	try:
		input_file_name=input("Entry file name?\n")
		input_file=open(input_file_name, "r")
	except FileNotFoundError:
		print("This file doesn't exist.")
		continue
	except:
		quit()
	break
output_file_name=input("Output file name?\n")
output_file=open(output_file_name, "w")
i=1
while 1:
	spaces=" "*(3-(math.floor(math.log(i, 10))))
	line=input_file.readline()
	if not line: break
	line="%d"%(i)+spaces+line
	output_file.write(line)
	i+=1
print("Number of lines:", i)
input_file.close()
output_file.close()