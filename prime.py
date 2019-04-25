r = 1

while(r < 100):
   r = r+1
   i = 0
   con = 0
   while(i <= r):
    i = i+1   
    if(r%i == 0):
	    con=con+1
   
   if(con ==2):
      print(r,end=" ")   