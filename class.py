class MGM:
	def walk3(self):
		print("walk-MGM")

class MGF:
	def Talk(self):
		print("Talk -MGF")	

class PGM:
	def walk(self):
		print("walk-PGM")		

class PGF:
	def Talk(self):
		print("Talk -PGF")
		print(dir(self))
		
class Mom(MGM,MGF):
	'''def __del__(self):
		print("Destructor for the class",id(self))	
	def __init__(self):
		print("object constructed successfully")'''
	def walk2(self):
		print("walk elegentlu", id(self))

class Dad(PGM,PGF):
	def Talk(self):
		print("Talk -Dad")

	


class Infant(Mom,Dad):
	'First class Python () are optional'
	'''def __del__(self):
		print("Destructor Infant for the class",id(self))
	def __init__(self):
		print("object Infant constructed successfully",id(self))'''
	def walk1(self):
		print("walk -infant")
	
		

#Mother = Mom()
#Mother.walk()
#del(Mother)
Baby = Infant()
Baby.Talk()
Baby.walk()

PGF.Talk(Baby)


#print("Mother id,id(Mother)")
#help(Baby)

#print(dir(Baby))