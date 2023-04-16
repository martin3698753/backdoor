import socket
import sys
import subprocess

class Listener:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('127.0.0.1', 3333))
        self.s.listen()
        self.con, add = self.s.accept()
        print("connection from " + str(add))

    def execute(self, command):
        self.con.send(command.encode())
        return self.con.recv(1024)

    def run(self):
        while True:
            command = input("> ")
            result = self.execute(command)
            print(result.decode())
            if(command == 'quit'):
                self.con.close()
                self.s.close()
                print("connection closed")
                sys.exit()


my_listener = Listener("127.0.0.1", 3333)
my_listener.run()


#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('127.0.0.1', 3333))
#s.listen()
#con, add = s.accept()
#print("connection from " + str(add))
#while True:
#    command = input("> ")
#    con.send(command.encode())
#    result = con.recv(1024)
#    print(result.decode())
#    if(command == 'quit'):
#        con.close()
#        s.close()
#        print("connection closed")
#        sys.exit()
#
#s.close()
