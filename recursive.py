import sys

sys.setrecursionlimit(10000)
def recursie(a):
   if a==1:
      return 1
   else:
      return a * recursie(a-1)  
  

print(recursie(1))







