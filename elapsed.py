#!/play/p1/bin/python

import time

last_executed=0
def fn1():
 global last_executed
 now=time.time()
 if last_executed==0:
  last_executed=now
 elapsed_time=now-last_executed
  
 print(last_executed)

fn1()
print(last_executed)
