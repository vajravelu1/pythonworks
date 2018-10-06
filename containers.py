#!/play/p1/bin/python

class Containers:
 serial=4364

 def _get_next_serial():
  Containers.serial+=1
  return Containers.serial
 
 def __init__(self,name,content):
  self.name=name
  self.content=content
  self.serial=Containers._get_next_serial()


print(f'the last serial number assigned was: {Containers.serial}')
c1=Containers('DSF','apples')
print(f'the serial no on container c1 is : {c1.serial}')
print(f'the last serial number assigned was: {Containers.serial}')
c2=Containers('FJK','mangoes')
print(f'the serial no on container c2 is : {c2.serial}')
print(f'the last serial number assigned was: {Containers.serial}')
