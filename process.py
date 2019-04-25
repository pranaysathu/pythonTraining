#!/usr/bin/python

#unix
import os
(R,W) = os.pipe()
ret=os.fork()


if 0 == ret:
	ctr=1
	stre = "In hcild ps: "+ str(os.getpid())
	os.write(W,stre)
	#while ctr <=1000 :
	#	print("Paresnt :", os.getpid())
	#	ctr+=1
else:
	newstr = os.Read(R,1024)
	print(newstr)
	#os.wait()
	#while ctr <=1000 :
	#	print("child :", os.getpid())
	#	ctr+=1	