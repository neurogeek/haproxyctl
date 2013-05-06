class Cmd(object):
    args = []
    cmdTxt = ""

    def __init__(self, *args, **kwargs):
        """Argument to the command are given 
           in kwargs only. We ignore *args."""

        self.args = kwargs

    def whatArgs(self):
        return self.args

    def getCmd(self):
        raise Exception("Must be Overriden")

    def getResult(self, res):
        return res

    def getResultObj(self, res):
        return res

class _ableServer(Cmd):
    cmdTxt = "server %(backend)s/%(server)s\r\n"
    args = ["backend", "server"]
    switch = ""

    def getCmd(self):
        if not self.switch:
            raise Exception("No action specified")
        cmdTxt = " ".join((self.switch, self.cmdTxt % self.args)) 
        return cmdTxt

class disableServer(_ableServer):
    switch = "disable"

class enableServer(_ableServer):
    switch = "enable"

class showErrors(Cmd):
    def getCmd(self):
        return "show errors\r\n"

class showInfo(Cmd):
    def getCmd(self):
        return "show info\r\n"

#    def getResultObj(self, res)
#    def getResult(self, res):
#       """Name: HAProxy
#           Version: 1.5-dev17
#           Release_date: 2012/12/28
#           Nbproc: 1
#           Process_num: 1
#           Pid: 26947
#           Uptime: 3d 12h02m59s
#           Uptime_sec: 302579
#           Memmax_MB: 0
#           Ulimit-n: 2092
#           Maxsock: 2092
#           Maxconn: 1024
#           Hard_maxconn: 1024
#           Maxpipes: 0
#           CurrConns: 0
#           PipesUsed: 0
#           PipesFree: 0
#           ConnRate: 0
#           ConnRateLimit: 0
#           MaxConnRate: 30
#           CompressBpsIn: 0
#           CompressBpsOut: 0
#           CompressBpsRateLim: 0
#           ZlibMemUsage: 0
#           MaxZlibMemUsage: 0
#           Tasks: 14
#           Run_queue: 1
#           Idle_pct: 100
#           node: dlb0
#           description:""" 
#       return res
