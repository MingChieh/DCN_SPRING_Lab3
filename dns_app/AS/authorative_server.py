import sockets

ip = '127.0.0.1'
port = 53533
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (ip, port)
s.bind(server_address)

while True:
    data, address = s.recvfrom(54533)
    reply_message['TYPE'] = data['TYPE']
    reply_message['NAME'] = data['NAME']
    reply_message['VALUE'] = ip
    reply_message['TTL'] = 10

    s.sendto(reply_message.encode('utf-8'))
