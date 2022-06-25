import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
ENC_FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message = msg.encode(ENC_FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(ENC_FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	
	client.send(send_length)
	client.send(message)

send('Hello World!')
