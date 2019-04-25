num=1
while num!= -1:
	try:
		num = int(input("Enter number:"))
	except ValueError:
		print("That was not a number")
	except:
		#raise KeyboardInterrupt
		print("Default")
	finally:
		print("In clean up cblock")