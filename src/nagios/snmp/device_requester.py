import requests
import re
import simplejson as json
from nagios.snmp.log import log


class DeviceRequester:
    def __init__(self, config):
        self._config = config

    def get_url(self):
        return "http://%s:%d%s" % (
            self._config['device_requester']['request_server'],
            self._config['device_requester']['request_port'],
            self._config['device_requester']['request_url']
        )

    def get_device(self, ipaddr):
        url = self.get_url()
        params = {'ip': ipaddr, 'scan': False}

        response = requests.get(url, params={'json': json.dumps(params)})
        if response.status_code != 200:
            log.error('DeviceRequester: Request for ip %s failed. ' % ipaddr + response.content)

        return response.json()

    def get_nagios_hostname(self, ipaddr):
        device = self.get_device(ipaddr)
        node_id = device['node']['id']
        name = device['node']['name']

        name = re.sub('[^a-zA-Z0-9-_]+', '', name)
        if len(name) > 10:
            name = name[0:9]

        return "%d_%s" % (node_id, name)
