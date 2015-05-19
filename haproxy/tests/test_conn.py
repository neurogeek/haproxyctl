from haproxy import conn, const
from unittest import TestCase
from socket import AF_INET, AF_UNIX


class SimpleConnMock(object):
    def __init__(self, stype, stream):
        self.stype = stype
        self.stream = stream

    def connect(self, addr):
        pass

class TestConnection(TestCase):

    def testConnSimple(self):
        sfile = "/some/path/to/socket.sock"
        c = conn.HaPConn(sfile, socket_module=SimpleConnMock)
        addr, stype = c.sfile
        self.assertEqual(sfile, addr)
        self.assertEqual(stype, AF_UNIX)

    def testConnUnixString(self):
        sfile = "unix:///some/path/to/socket.socket"
        c = conn.HaPConn(sfile, socket_module=SimpleConnMock)
        addr, stype = c.sfile
        self.assertEqual("/some/path/to/socket.socket", addr)
        self.assertEqual(stype, AF_UNIX)

    def testConnTCPString(self):
        sfile = "tcp://1.2.3.4:8080"
        c = conn.HaPConn(sfile, socket_module=SimpleConnMock)
        addr, stype = c.sfile
        ip, port = addr
        self.assertEqual("1.2.3.4", ip)
        self.assertEqual(8080, port)
        self.assertEqual(stype, AF_INET)

    def testConnTCPStringNoPort(self):
        sfile = "tcp://1.2.3.4"
        with self.assertRaises(Exception):
            c = conn.HaPConn(sfile, socket_module=SimpleConnMock)
