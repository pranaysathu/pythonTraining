#!/usr/bin/python

def recursie(a):
   if a==1:
      return 1
   else:
      return a * recursie(a-1) 


def recursie1(a):
   if a==1:
      return 1
   else:
      return a * recursie1(a-1)
	  
	  
if '__main__' == __name__:
	print(recursie(3))
else:
	print(__name__)