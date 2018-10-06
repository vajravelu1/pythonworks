import socket

class Resolve:
	def __init__(self):
		self._cache={}

	def __call__(self,host):
		self.hostname=host
		if host not in self._cache:
			self._cache[host]=socket.gethostbyname(host)
		return self._cache[host]
