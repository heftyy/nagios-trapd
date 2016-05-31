import json


class TrapEvent(object):

    EVENT_SEVERITY = {"CRITICAL": 2, "WARNING": 1, "OK": 0}

    def __init__(self, name, output, status, handlers, ipaddr):
        self.name = name
        self.output = output
        self.status = status
        self.handlers = handlers
        self.ipaddr = ipaddr

    def to_json(self):
        return json.dumps({'name': self.name,
                           'output': self.output,
                           'status': self.status,
                           'handlers': self.handlers,
                           'ipaddr': self.ipaddr})

    def __repr__(self):
        return "<TrapEvent name:'%s' >" % self.name
