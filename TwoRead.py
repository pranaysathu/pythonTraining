import sys
filename= sys.argv[1]


fobj = open("C:\\Users\\Training\\Desktop\\Pranay\\"+filename)

content = fobj.readline()
i=0
while(content!=''):
   i=i+1
   if i ==1:
      print(content)
   fobj.seek(fobj.tell()-len(content)-1)
   content=fobj.readline()
   print(content)
   content=fobj.readline()
   print(content)

