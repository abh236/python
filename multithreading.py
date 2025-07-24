import threading
import time

def you_run(name):
  time.sleep(10)
  print(f"{name} running complete")

def you_getmail(name,time1):
  time.sleep(5)
  print(f"{name} getting mail at {time1} ")

def you_getphone():
  time.sleep(3)
  print("You are getting phone ")

chore1=threading.Thread(target=you_run,args=["abhi",])
chore1.start()
chore2=threading.Thread(target=you_getmail,args=["abhi",10])
chore2.start()
chore3=threading.Thread(target=you_getphone)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

you_run('Abhi')  
you_getmail('Abhi',10)
you_getphone()