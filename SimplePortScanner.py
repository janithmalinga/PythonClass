import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scanner(port):
	try:
		conn = socket.connect(("egscyber.com",port))
		return True
	except:
		return False

for port in range(5):
	if scanner(port):
		print('Port', port, 'is open')
	else:
		print('Port', port, 'is closed')
