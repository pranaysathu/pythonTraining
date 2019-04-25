def average(l):
	'''
	>>> print(average([10,20,30]))
	20
	>>> print(average([10,20,30,20]))
	20
	>>> print(average([10,20,30,20]))
	20
	'''
	return sum(l)/len(l)


import doctest
doctest.testmod()


