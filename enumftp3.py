#!/usr/bin/python3

import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(("192.168.0.87", 21))

banner = tcp.recv(1024)
print(banner.decode('utf-8'))

print("Enviando usuario...")
tcp.send(b"USER ftp\r\n")
user = tcp.recv(1024)
print(user.decode('utf-8'))

print("Enviando a senha...")
tcp.send(b"PASS ftp\r\n")
pw = tcp.recv(1024)
print(pw.decode('utf-8'))

print("Enviando Comando PWD...")
tcp.send(b"PWD \r\n")
cmd = tcp.recv(2048)
print(cmd.decode('utf-8'))
