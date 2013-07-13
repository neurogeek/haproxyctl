"""cmds.py
   Implementations of the different HAProxy commands"""

import re

class Cmd(object):
    """Cmd - Command base class"""

    p_args = []
    args = {}
    cmdTxt = ""

    def __init__(self, *args, **kwargs):
        """Argument to the command are given 
           in kwargs only. We ignore *args."""

        self.args = kwargs
        if not all([a in kwargs.keys() for a in self.p_args]):
            raise Exception("Wrong number of arguments. Required arguments are " + 
                                self.whatArgs())

    def whatArgs(self):
        return ",".join(self.p_args)

    @classmethod
    def getHelp(self):
        txtArgs = ",".join(self.p_args)

        if not txtArgs:
            txtArgs = "None"
        return " ".join((self.helpTxt, "Arguments: %s" % txtArgs))

    def getCmd(self):

        # The default behavior is to apply the 
        # args dict to cmdTxt
        return self.cmdTxt % self.args

    def getResult(self, res):
        """Returns raw results gathered from 
           HAProxy"""
        return res

    def getResultObj(self, res):
        """Returns refined output from 
           HAProxy, packed inside a Python obj
           i.e. a dict()"""
        return res

class _ableServer(Cmd):
    """Base class for enable/disable commands"""

    cmdTxt = "server %(backend)s/%(server)s\r\n"
    p_args = ["backend", "server"]
    switch = ""

    def getCmd(self):
        if not self.switch:
            raise Exception("No action specified")
        cmdTxt = " ".join((self.switch, self.cmdTxt % self.args)) 
        return cmdTxt

class disableServer(_ableServer):
    switch = "disable"
    helpTxt = "Disables given backend/server"

class enableServer(_ableServer):
    switch = "enable"
    helpTxt = "Enables given backend/server"

class setWeight(Cmd):
    cmdTxt = "set weight %(backend)s/%(server)s %(weight)s\r\n"
    p_args = ['backend', 'server', 'weight']
    helpTxt = "Set weight for a given backend/server."

class getWeight(Cmd):
    cmdTxt = "get weight %(backend)s/%(server)s\r\n"
    p_args = ['backend', 'server']
    helpTxt = "Get weight for a given backend/server."

class showErrors(Cmd):
    """Show errors HAProxy command"""
    cmdTxt = "show errors\r\n"
    helpTxt = "Shows errors on HAProxy instance."

    def getResultObj(self, res):
        return res.split('\n')

class showInfo(Cmd):
    """Show info HAProxy command"""
    cmdTxt = "show info\r\n"
    helpTxt = "Shows errors on HAProxy instance."

    def getResultObj(self, res):
        resDict = {}
        for line in res.split('\n'):
            k, v = line.split(':')
            resDict[k] = v

        return resDict

class baseStat(Cmd):
    def getCols(self, res):
        mobj = re.match("^#(?P<columns>.*)$", res, re.MULTILINE)

        if mobj:
            return dict((a, i) for i, a in enumerate(mobj.groupdict()['columns'].split(',')))
        raise Exception("Could not parse columns from HAProxy output")

class listServers(baseStat):
    """Show servers in the given backend"""

    p_args = ['backend']
    cmdTxt = "show stat\r\n"
    helpTxt = "Lists servers in the given backend"

    def getResult(self, res):
        return "\n".join(self.getResultObj(res))

    def getResultObj(self, res):
        
        servers = []
        cols = self.getCols(res)

        for line in res.split('\n'):
            if line.startswith(self.args['backend']):
                # Lines for server start with the name of the 
                # backend.

                outCols = line.split(',')
                if outCols[cols['svname']] != 'BACKEND':
                    servers.append(" " .join(("Name: %s" % outCols[cols['svname']],
                             "Status: %s" % outCols[cols['status']], 
                             "Weight: %s" %  outCols[cols['weight']],
                             "bIn: %s" % outCols[cols['bin']],
                             "bOut: %s" % outCols[cols['bout']])))

        return servers
