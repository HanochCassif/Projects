import socket

# open UDP socket

udp_address = "192.168.1.4"
udp_port = 5001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# elmo_cmd = b"px =555;"



# Send elmo command
# sock.sendto(elmo_cmd, (udp_address, udp_port))


# Receive elmo data
elmo_cmd=b"sw;"
sock.sendto(elmo_cmd, (udp_address, udp_port))

# buffer size is 20 bytes
# data, addr = sock.recvfrom(20)

data = sock.recv(20)
print(str(elmo_cmd))
print(str(elmo_cmd)[4])
# data_s = string()

print("received message: %s" % str(data))

# data, addr = sock.recvfrom(1024)
# print("status register is: %s" % unicodedata.decimal(data.decode()))

sock.close()