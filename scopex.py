#!/usr/bin/python
a,b,c,d=10,20,30,40
def funA():
   a,b,c=100,200,300
   print("In A", a,b,c,d)
   def funB():
      a,b=1000,2000
      print("In b",a,b,c,d)
      def funC():
	      a=10000
	      print("In C", a,b,c,d)
      funC()
   funB()
funA()


print("IN__main__",a,b,c,d)



def sopmea():
	def someb():
		print("yoy")
		return 5+6
	return someb()


#print(somed())
print(sopmea())		