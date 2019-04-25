import sys
filename= sys.argv[1]

fobj = open("C:\\Users\\Training\\Desktop\\Pranay\\"+filename)

l =0
for i in fobj.readlines():
   l = l+1
   print(l,i)