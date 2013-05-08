"""Connection module"""
from socket import socket, AF_UNIX, SOCK_STREAM
from haproxy import const

class HaPConn(object):
    """HAProxy Socket object.
       This class abstract the socket interface so 
       commands can be sent to HAProxy and results received and
       parse by the command objects"""

    def __init__(self, sfile):
        """Initializes an HAProxy and opens a connection to it
           sfile -> Path for the UNIX socket"""
        self.sfile = sfile
        self.sock = None
        self.open()

    def open(self):
        """Opens a connection for the socket. 
           This function should only be called if 
           self.closed() method was called"""

        self.sock = socket(AF_UNIX, SOCK_STREAM) 
        self.sock.connect(self.sfile)

    def sendCmd(self, cmd, objectify=False):
        """Receives a command obj and sends it to the
           socket. Receives the output and passes it through
           the command to parse it a present it. 
           - objectify -> Return an object instead of plain text"""
           
        res = ""
        self.sock.send(cmd.getCmd())
        output = self.sock.recv(const.HaP_BUFSIZE)
       
        while output:
            res += output
            output = self.sock.recv(const.HaP_BUFSIZE)

        if objectify:
            return cmd.getResultObj(res)

        return cmd.getResult(res)

    def close(self):
        """Closes the socket"""
        self.sock.close()
