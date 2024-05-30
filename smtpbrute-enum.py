#!/usr/bin/python3
import socket
import sys
import re

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <endereço IP>")
        sys.exit(1)

    ip = sys.argv[1]

    try:
        with open("listausuarios.txt") as file:
            for linha in file:
                linha = linha.strip()
                if linha:
                    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tcp.connect((ip, 25))
                    banner = tcp.recv(1024).decode('utf-8')
                    tcp.sendall(f"VRFY {linha}\r\n".encode('utf-8'))
                    user = tcp.recv(1024).decode('utf-8')
                    if re.search("252", user):
                        print(f"Usuário encontrado: {user.strip('252 2.0.0').strip()}")
                    tcp.close()
    except FileNotFoundError:
        print("Erro: O arquivo listausuarios.txt não foi encontrado.")
    except socket.error as e:
        print(f"Erro de socket: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
