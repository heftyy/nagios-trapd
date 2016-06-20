import requests
import re
import simplejson as json
from nagios.snmp.log import log


class DeviceRequester:
    def __init__(self, config):
        self._config = config

    def get_device_url(self):
        url = self._config['device_requester']['device_request_url']
        return url if url.startswith('http://') else "http://%s" % url

    def get_nagios_settings_url(self):
        url = self._config['device_requester']['nagios_settings_settings']
        return url if url.startswith('http://') else "http://%s" % url

    def get_device(self, ipaddr):
        url = self.get_device_url()
        params = {'ip': ipaddr, 'scan': False}

        response = requests.get(url, params={'json': json.dumps(params)})
        if response.status_code != 200:
            log.error('DeviceRequester: Request for ip %s failed. ' % ipaddr + response.content)

        return response.json()

    def get_nagios_settings(self, ipaddr):
        device = self.get_device(ipaddr)
        node_id = device['node']['id']
        url = self.get_nagios_settings_url()

        response = requests.get('%s/%s' % (url, node_id))
        if response.status_code != 200:
            log.error('DeviceRequester: Request for nagios settings for ip %s failed. ' % ipaddr + response.content)

        return response.json()

    def get_nagios_hostname(self, ipaddr):
        device = self.get_device(ipaddr)
        node_id = device['node']['id']
        name = device['node']['name']

        name = re.sub('[^a-zA-Z0-9-_]+', '', name)
        if len(name) > 10:
            name = name[0:9]

        return "%d_%s" % (node_id, name)

    def get_trap_settings(self, ipaddr):
        response = self.get_nagios_settings(ipaddr)
        settings_string = response['settingsString']
        settings = json.loads(settings_string)

        if 'trap' not in settings:
            log.error('DeviceRequester: Trap config not available for ip %s' % ipaddr)

        return settings['trap']

