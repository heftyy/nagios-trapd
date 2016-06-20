import os
import re
import threading
import time
import json
import traceback
from collections import deque
from subprocess import call

from pysnmp.proto.rfc1902 import ObjectName

from nagios.snmp.log import events_log
from nagios.snmp.log import log
from nagios.snmp.device_requester import DeviceRequester


class TrapEventDispatcherThread(threading.Thread):
    def __init__(self, config):
        # Initialize threading.Thread
        threading.Thread.__init__(self, name=self.__class__.__name__)
        # Initialize TrapEventDispatcher
        self._config = config
        self._trap_event_dispatcher = TrapEventDispatcher(config)
        self._run = False
        self._events = deque()

    def dispatch(self, event):
        # Log Event
        events_log.info(event.to_json())
        # Enqueue TrapEvent
        self._events.append(event)
        log.debug("TrapEventDispatcherThread: Enqueued Event: %r" % event)
        return True

    def stop(self):
        self._run = False

    def run(self):
        log.debug("%s: Started" % self.name)
        self._run = True
        backoff = 0
        while self._run:
            if backoff <= 0:
                try:
                    # pop event off queue
                    event = self._events.popleft()

                    success = False
                    # attempt to dispatch event
                    try:
                        success = self._trap_event_dispatcher.dispatch(event)
                    except Exception as err:
                        print(traceback.format_exc())

                    if not success:
                        # dispatch failed. put the event back on the queue
                        self._events.appendleft(event)

                        # back off
                        backoff = int(self._config['dispatcher']['backoff'])

                        log.debug("TrapDispatcherThread: back off for %d seconds" % backoff)

                except IndexError:
                    # Nothing in queue
                    pass

            else:
                backoff -= 1

            time.sleep(1)

        log.debug("%s: Exiting" % self.name)


class TrapEventDispatcher(object):
    def __init__(self, config):
        self._config = config
        self._device_requester = DeviceRequester(config)

        log.debug("TrapEventDispatcher: Initialized")

    def dispatch(self, event):
        hostname = self._device_requester.get_nagios_hostname(event.ipaddr)
        traps = self._device_requester.get_trap_settings(event.ipaddr)

        trap_valid = False
        for trap in traps:
            if event.name == trap['name']:
                oid = ObjectName(trap['oid'])
                if str(event.arguments[oid]) == str(trap['value']):
                    trap_valid = True
                    break

        if not trap_valid:
            log.error('TrapEventDispatcher: Trap is not valid %s' % event.to_json())
            return

        command = self._config['dispatcher']['command']
        command_exists = os.path.isfile(command)
        if not command_exists:
            log.error('TrapEventDispatcher: Dispatcher command does not exist.')
            return False

        success = len(event.handlers) > 0

        for handler in event.handlers:
            output_dict = {
                'nagios_status': event.status,
                'output': event.output,
                'type': event.name
            }

            output = '!' + json.dumps(output_dict)

            log.debug('TrapEventDispatcher: command called %s %s %s %s %s' % (command,
                                                                              hostname,
                                                                              handler,
                                                                              str(event.status),
                                                                              output))

            ret = call([command, hostname, handler, str(event.status), output])

            print(event.to_json())
            log.debug('TrapEventDispatcher: Message has been sent to nagios (%s).' % hostname)
            success = ret == 0

        return success
