import sys
filename= sys.argv[1]
wfilename = sys.argv[2]

fobj = open("C:\\Users\\Training\\Desktop\\Pranay\\"+filename)
wfile = open("C:\\Users\\Training\\Desktop\\Pranay\\"+wfilename,'w')

for i in fobj.readlines():
   wfile.write(i)
