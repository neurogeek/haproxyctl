from haproxy import cmds
from unittest import TestCase

class TestCommands(TestCase):
    def setUp(self):
        self.Resp = {"disable" : "disable server redis-ro/redis-ro0",
                     "info" : "show info",
                     "errors" : "show errors",
                     "enable" : "enable server redis-ro/redis-ro0"}
        self.Resp = dict([(k, v + "\r\n") for k, v in self.Resp.iteritems()])

    def test_disableServer(self):
        """Test 'disable server' command"""
        args = {"backend" : "redis-ro", "server" : "redis-ro0"}
        cmdDisable = cmds.disableServer(**args).getCmd()
        self.assertEqual(cmdDisable, self.Resp["disable"])

    def test_enableServer(self):
        """Test 'enable server' command"""
        args = {"backend" : "redis-ro", "server" : "redis-ro0"}
        cmdEnable = cmds.enableServer(**args).getCmd()
        self.assertEqual(cmdEnable, self.Resp["enable"])

    def test_showInfo(self):
        """Test 'show info' command"""
        cmdShowInfo = cmds.showInfo().getCmd()
        self.assertEqual(cmdShowInfo, self.Resp["info"])

    def test_showErrors(self):
        """Test 'show errors' command"""
        cmdShowErrors = cmds.showErrors().getCmd()
        self.assertEqual(cmdShowErrors, self.Resp["errors"])
