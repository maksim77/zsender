import unittest
from ZabbixSender import ZabbixSender

import os
import json

# IP = '127.0.0.1'
IP = '192.168.99.100'  # For local testing


class ZabbixSenderTests(unittest.TestCase):
    def setUp(self):
        self.server = ZabbixSender(IP, 10051)

    def test_server_init_host(self):
        self.assertEqual(self.server.server, IP)

    def test_server_init_port(self):
        self.assertEqual(self.server.port, 10051)

    def test_server_init_status(self):
        self.assertEqual(self.server.status, '')

    def test_server_print_info(self):
        server_dict = {'server': str(IP), "port": 10051}
        self.assertEqual(json.loads(self.server.__str__()), server_dict)

    def test_conf_file_parse(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, 'zabbix_agentd.conf')
        server = ZabbixSender(config=filename)
        self.assertEqual(server.server, '192.168.1.2')
