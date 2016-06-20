import simplejson as json


class TrapEvent(object):

    EVENT_SEVERITY = {"CRITICAL": 2, "WARNING": 1, "OK": 0}

    def __init__(self, name, event_type, output, status, handlers, ipaddr, arguments):
        self.name = name
        self.type = event_type
        self.output = output
        self.status = status
        self.handlers = handlers
        self.ipaddr = ipaddr
        self.arguments = arguments

    def to_json(self):
        return json.dumps({'name': self.name,
                           'type': self.type,
                           'output': self.output,
                           'status': self.status,
                           'handlers': self.handlers,
                           'ipaddr': self.ipaddr})

    def __repr__(self):
        return "<TrapEvent name:'%s' >" % self.name
