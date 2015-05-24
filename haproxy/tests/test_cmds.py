# pylint: disable=star-args, locally-disabled, too-few-public-methods, no-self-use, invalid-name
"""test_cmds.py - Unittests related to command implementations."""
from haproxy import cmds
from unittest import TestCase

class TestCommands(TestCase):
    """Tests all of the haproxyctl's various commands."""
    def setUp(self):

        self.Resp = {"disable" : "disable server redis-ro/redis-ro0",
                     "info" : "show info",
                     "errors" : "show errors",
                     "set-weight" : "set weight redis-ro/redis-ro0 20",
                     "get-weight" : "get weight redis-ro/redis-ro0",
                     "frontends" : "show stat",
                     "enable" : "enable server redis-ro/redis-ro0",
                     "set-server-agent" : "set server redis-ro/redis-ro0 agent up",
                     "set-server-health" : "set server redis-ro/redis-ro0 health stopping",
                     "set-server-state" : "set server redis-ro/redis-ro0 state drain"}

        self.Resp = dict([(k, v + "\r\n") for k, v in self.Resp.items()])

    def test_showFrontends(self):
        """Test 'frontends/backends' commands"""
        args = {}
        cmdFrontends = cmds.showFrontends(**args).getCmd()
        self.assertEqual(cmdFrontends, self.Resp["frontends"])

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

    def test_getWeight(self):
        """Test 'get weight' command"""
        args = {"backend" : "redis-ro", "server" : "redis-ro0"}
        cmdGetWeight = cmds.getWeight(**args).getCmd()
        self.assertEqual(cmdGetWeight, self.Resp["get-weight"])

    def test_setWeight(self):
        """Test 'set weight' command"""
        args = {"backend" : "redis-ro", "server" : "redis-ro0", "weight" : "20"}
        cmdSetWeight = cmds.setWeight(**args).getCmd()
        self.assertEqual(cmdSetWeight, self.Resp["set-weight"])

    def test_showInfo(self):
        """Test 'show info' command"""
        cmdShowInfo = cmds.showInfo().getCmd()
        self.assertEqual(cmdShowInfo, self.Resp["info"])

    def test_showErrors(self):
        """Test 'show errors' command"""
        cmdShowErrors = cmds.showErrors().getCmd()
        self.assertEqual(cmdShowErrors, self.Resp["errors"])

    def test_setServerAgent(self):
        """Test 'set server agent' command"""
        args = {"backend": "redis-ro", "server" : "redis-ro0", "value": "up"}
        cmdSetServerAgent = cmds.setServerAgent(**args).getCmd()
        self.assertEqual(cmdSetServerAgent, self.Resp["set-server-agent"])

    def test_setServerHealth(self):
        """Test 'set server health' command"""
        args = {"backend": "redis-ro", "server" : "redis-ro0", "value": "stopping"}
        cmdSetServerHealth = cmds.setServerHealth(**args).getCmd()
        self.assertEqual(cmdSetServerHealth, self.Resp["set-server-health"])

    def test_setServerState(self):
        """Test 'set server state' command"""
        args = {"backend": "redis-ro", "server" : "redis-ro0", "value": "drain"}
        cmdSetServerState = cmds.setServerState(**args).getCmd()
        self.assertEqual(cmdSetServerState, self.Resp["set-server-state"])
