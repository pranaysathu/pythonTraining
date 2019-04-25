filename= input("Enter file name: ")

fobj = open("C:\\Users\\Training\\Desktop\\Pranay\\"+filename)
l =0
content = fobj.readline()
while(content!=''):
   l = l+1
   print(l,content)
   content = fobj.readline()  



   
