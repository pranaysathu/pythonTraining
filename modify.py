#!/usr/bin/python

RateodInterest=5

def calc(p,t):
	global RateodInterest
	global localvalue
	print(p*t*RateodInterest/100)
	RateodInterest=6
	localvalue =50

#global localvalue=55
	

calc(100000,1)
print(RateodInterest)
print(localvalue)