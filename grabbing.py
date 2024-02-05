#!/usr/bin/python3
import socket
while True:
	ip = input("digite o ip:")
	porta = int(input("digite a porta"))

	meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	meusocket.connect((ip,porta))

	banner = meusocket.recv(1024)
	print(banner)
