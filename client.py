import socket
import sys

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server

COMMANDS = ["/EXIT", "/NICK"]

def check_name(string):
    string = string[:3].decode()
    if string == "^^^":
        return True
    else:
        return False

def remove_check(string):
    string = string[3:].decode()
    string = string.replace("''", "")
    return string

def command(string):
    if string == "":
        return " "
    if any(x in string for x in COMMANDS):
        match_string = string[:5]
        match match_string:
            case "/EXIT":
                sys.exit()
            case "/NICK":
                nick_string = string[6:]
                if not nick_string or nick_string.isspace():
                    string = " "
                return string
            case _:
                return string
    else:
        return string



def input_loop():
    msg = input("Enter your message: ")
    print('\033[1A' + '\033[K', end='')
    msg = command(msg)
    msg = msg.encode()
    s.sendall(msg)
    data = s.recv(1024)
    addr = s.recv(1024)
    if check_name(addr):
        addr = remove_check(addr)
    if addr and data.decode():
        print(repr(addr) + ": " + data.decode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        input_loop()
#     s.sendall(msg)
#     data = s.recv(1024)
#     addr = s.recv(1024)
#     if check_name(addr):
#         addr = remove_check(addr)
#
# print("Client received data: " + data.decode() + ", from user: " + repr(addr))
