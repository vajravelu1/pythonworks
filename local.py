#!/play/p1/bin/python

message='global'

def enclosing():
 global message
 message='enclosing'
 def local():
  global message
  message='local'
 print(f'from enclosing :{message}')
 local()
 print(f'from enclosing :{message}')

print(f'from global :{message}')
enclosing()
print(f'from global :{message}')
