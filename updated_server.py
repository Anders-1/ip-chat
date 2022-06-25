import socket
import sys
import pickle

try:
    # Getting back the objects:
    with open('variables.pkl', 'rb') as f:
      nicks = pickle.load(f)
    print("[SERVER] Could retrieve the variables!")
    print(nicks)
except:
    nicks = {}
    print("[SERVER] Couldn't retrieve the variables!")

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

COMMANDS = ["/NICK", "/CLSN", "/STOP"]

def command(string, addr):
    global nicks

    if any(x in string for x in COMMANDS):
        match_string = string[:5]
        print("[SERVER] MATCHING: " + string)
        match match_string:
            case "/NICK":
                nicks[addr] = string[6:]
                print("[SERVER] NICKS: " + str(nicks))
            case "/CLSN":
                nicks = {}
            case "/STOP":
                save_nicks()
                sys.exit()
    else:
        return

def save_nicks():
    global nicks
    # Saving the objects:
    print("[SERVER] Saving nicks: " + str(nicks))
    with open('variables.pkl', 'wb') as f:
        pickle.dump(nicks, f)

def check_nicks(string):
    global nicks
    print("[SERVER] When checking nicks, nicks is: " + str(nicks))

    print("[SERVER] Checking nicks of: " + string)
    if string in nicks:
        print("[SERVER] Nick of: " + string + " is: " + nicks[string])
        return nicks[string]
    else:
        print("[SERVER] No nicks of: " + string)
        return


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        with conn:
            print('[SERVER] Connected by: ', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                print("[SERVER] Received data: " + repr(data) + ", from user: " + repr(addr[0]))
                # COMMANDS
                command(data.decode(), addr[0])
                if check_nicks(addr[0]):
                    name = check_nicks(addr[0])
                    print("[SERVER] NAME: " + name)
                else:
                    name = addr[0]
                    print("[SERVER] NAME: " + name)
                conn.sendall(data)
                conn.sendall(("^^^" + name).encode())
