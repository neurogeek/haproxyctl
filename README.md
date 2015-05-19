HAProxyctl
==========

HAProxy control tool

Build Status
------------

[![Build Status](https://travis-ci.org/neurogeek/haproxyctl.png?branch=master)](https://travis-ci.org/neurogeek/haproxyctl)

About
--------

HAProxyctl is a tool to manage the various aspects of HAProxy that can be controlled by means of its socket.

With HAProxyctl, it is possible to do the following:

(New in 0.3)
* frontends  -  Lists available Frontends. Arguments: None
* backends  -  Lists available Backends. Arguments: None

(New in 0.2)
* info  -  Shows errors on HAProxy instance. Arguments: None
* enable  -  Enables given backend/server Arguments: backend,server
* disable  -  Disables given backend/server Arguments: backend,server
* get-weight  -  Get weight for a given backend/server. Arguments: backend,server	
* set-weight  -  Set weight for a given backend/server. Arguments: backend,server,weight
* servers  -  Lists servers in the given backend Arguments: backend

Modes
-----

HAProxyctl can be used in 2 modes. CLI mode and Python API mode. 
CLI mode, as the name implies, gives you a command, haproxyctl, that can be used to control HAProxy.

You can use the Python API mode to integrate HAProxyctl directly in your Python project.

Every command in HAProxyctl has at least two methods: getResut and getResultObj. 

The method getResult returns a formatted string with the results obtained by executing the given HAProxy command, while getResultObj returns a Python object with the results, making it easy to use this results in some Python code.

CLI Usage
---------

```
usage: haproxyctl [-h] [-v] [-c COMMAND] [-l] [-H] [-s SERVER] [-b BACKEND]
                  [-w WEIGHT] [-k SOCKET]

Tool to interact with HAProxy

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Be verbose.
  -c COMMAND, --command COMMAND
                        Type of command. Default info
  -l, --list-commands   Lists available commands.
  -H, --help-command    Shows help for the given command.
  -s SERVER, --server SERVER
                        Attempt action on given server.
  -b BACKEND, --backend BACKEND
                        Set backend to act upon.
  -w WEIGHT, --weight WEIGHT
                        Specify weight for a server.
  -k SOCKET, --socket SOCKET
                        Socket to talk to HAProxy. It accepts
                        unix:///path/to/socket or tcp://1.2.3.4[:port]
                        addresses. If there is no match
                        for protocol, then it assumes a UNIX socket file.
```

API Usage
---------

TBW...
