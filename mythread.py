import threading
import time
class Mythread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter= counter
		print("something")
	def run(self):
		print("starting:",self.name)
		threadLock.acquire()
		print_time(self.name,self.counter,5)
		threadLock.release()
		
threadLock = threading.Lock()


def print_time(ThreadName, delay, counter):
	while counter:
		time.sleep(delay)
		print("%s : %s" %(ThreadName,time.ctime(time.time())))
		counter-=1


print("started main:")

thr1 = Mythread(1,"Thr 1",1)
thr2 = Mythread(2,"Thr 2",2)


thr1.start()
thr2.start()
thr1.join()
thr2.join()
'join is to synchrozize the threads'

print("End Main:")