class date():
	def __init__(self):
		self.dd=24
		self.mm=4
		self.yy=2019	
	def display(self):
		print(self.dd,self.mm,self.yy)
	def __add__(self,value):
		self.dd += value
		r = self.dd -30
		print("r",r)		
		if(r>0):
			self.dd = r%30
			i = r//30
			print("i",i)
			if(i>12):
				k = i//12
				print("k",k)
				self.yy+=k
				self.mm += i%12
			else:	
				self.mm+=1
				if(self.mm >12):
					k = self.mm % 12
					l = self.mm // 12
					self.mm = k
					self.yy+=l
		return self
		
		
today=date()
print(dir(today))
today.display()
print(today.dd)
tomorrow = today+600
tomorrow.display()