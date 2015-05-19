"""Connection module"""
import re
from socket import socket, AF_INET, AF_UNIX, SOCK_STREAM
from haproxy import const

class HaPConn(object):
    """HAProxy Socket object.
       This class abstract the socket interface so 
       commands can be sent to HAProxy and results received and
       parse by the command objects"""

    def __init__(self, sfile, socket_module=socket):
        """Initializes an HAProxy and opens a connection to it
           (sfile, type) -> Path for the UNIX socket"""

        self.sock = None
        sfile = sfile.strip()
        stype = AF_UNIX
        self.socket_module = socket_module

        mobj = re.match(
            '(?P<proto>unix://|tcp://)(?P<addr>[^:]+):*(?P<port>[0-9]*)$', sfile)

        if mobj:
            proto = mobj.groupdict().get('proto', None)
            addr = mobj.groupdict().get('addr', None)
            port = mobj.groupdict().get('port', '')

            if not addr or not proto:
                raise Exception('Could not determine type of socket.')

            if proto == const.HaP_TCP_PATH:
                stype = AF_INET
                port = True and port or const.HaP_DEFAULT_TPC_PORT
                sfile = (addr, port)

            if proto == const.HaP_UNIX_PATH:
                stype = AF_UNIX
                sfile = addr

        # Fallback should be sfile/AF_UNIX by default
        self.sfile = (sfile, stype)
        self.open()

    def open(self):
        """Opens a connection for the socket. 
           This function should only be called if 
           self.closed() method was called"""

        sfile, stype = self.sfile
        self.sock = self.socket_module(stype, SOCK_STREAM)
        self.sock.connect(sfile)

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
