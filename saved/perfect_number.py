#!/usr/bin/python3
#enter number in argument
import time
import sys

starttime = time.time()
n=int(sys.argv[1])
s=1
if n%2!=0:
	k=2
else: k=1
for i in range(2, n//2+1, k):
	if n%i==0:
			s+=i
if n==s:
	print(n, "is a perfect number.")
else:
	print(n, "is not a perfect number")
print("That took {} seconds".format(time.time()-starttime))