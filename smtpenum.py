#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 3:
    print("Modo de uso: python smtpenum.py IP USUARIO")
    sys.exit(0)

try:
    # Usando 'with' para garantir que o socket seja fechado corretamente
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
        tcp.connect((sys.argv[1], 25))

        # Recebe a mensagem inicial (banner) do servidor SMTP
        banner = tcp.recv(1024).decode('utf-8')
        print(banner)

        # Envia o comando VRFY seguido do usuário para verificar
        tcp.sendall(b"VRFY " + sys.argv[2].encode('utf-8') + b"\r\n")
        user = tcp.recv(1024).decode('utf-8')
        print(user)
except socket.error as e:
    print(f"Erro de socket: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    sys.exit(1)

