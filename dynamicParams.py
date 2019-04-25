def total(*parameters):
	result=0
	for value in parameters:
		result+=value

	return result
print(total(10,20,30))
print(total(1,2))
print(total(10000,5000,500,800))
print(total())




def func(**Kwords):
	for key in Kwords.keys():
		print(key,":",Kwords[key])
	
func(a=10,b="20",name="sathu",sat=9, sat2="@#~!+$#$%")