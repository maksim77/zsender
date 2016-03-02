import unittest
from ZabbixSender import ZabbixSender, ZabbixPacket

from datetime import datetime

# IP = '127.0.0.1'
IP = '192.168.99.100'  # For local testing


class FullTest(unittest.TestCase):
    def test_Full(self):
        self.server = ZabbixSender(IP, 10051)
        cur_date_unix = int(datetime.now().timestamp())
        packet = ZabbixPacket()
        packet.add('host2', 'key3', 'IDDQD')
        packet.add('host1', 'key1', 33.1, cur_date_unix)
        self.server.send(packet)
        self.assertEqual(self.server.status['response'], 'success')
