import time

def make_timer():
 last_executed=None
 
 def elapsed():
  nonlocal last_executed
  now=time.time()
  
  if last_executed==None:
   last_executed=now

  result=now-last_executed
  last_executed=now
  return result

 return elapsed
