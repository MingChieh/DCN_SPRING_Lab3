from flask import Flask, request
import socket

@app.route("/")
def page_request():
    return


@app.route("/register", methods=['PUT'):
def page_request():
    data = request.get_json()
    hostname = data['hostname']
    ip = data['ip']
    as_ip = data['as_ip']
    as_port = data['as_port']
    return 201

def registeration2AS():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 53533
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = 'TYPE=A, NAME=fibonnacci.com, VALUE=IP_ADDRESS, TTL=10'
    sock.bind((UDP_IP, UDP_PORT))
    return

if __name__ == '__main__':
    app.run(debug=True, port=9090)

