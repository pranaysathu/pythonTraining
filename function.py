"this is main doc"
def total(a,b):
   '''Disaply sum of two numbers
   or concatenated string'''
   print(__doc__)
   print(a+b)
   return(a+b)
   

print(total(5,10))

print(total.__doc__)

help(total)

total("good","Morning")




def tt(a,b,c=0):
   return(a+b+c)

print(tt(5,6))
print(tt(5,6,5))


