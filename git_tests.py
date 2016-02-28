import ZabbixSender
import unittest

from datetime import datetime


class TestServerConstructor(unittest.TestCase):
    def setUp(self):
        self.server = ZabbixSender.ZabbixSender('127.0.0.1', 10051)

    def test_conf_file_parse(self):
        server = ZabbixSender.ZabbixSender(config='zabbix_agentd.conf')
        self.assertEqual(server.server, '192.168.1.2')

    def test_server_host(self):
        self.assertEqual(self.server.server, '127.0.0.1')

    def test_server_port(self):
        self.assertEqual(self.server.port, 10051)

    def test_server_status(self):
        self.assertEqual(self.server.status, '')

    def test_full(self):
        cur_date_unix = datetime.now().timestamp()
        packet = ZabbixSender.ZabbixPacket()
        packet.add('host1', 'key1', 22.2)
        packet.add('host2', 'key3', 'IDDQD')
        packet.add('host1', 'key1', 33.1, cur_date_unix)
        self.server.send(packet)
        self.assertEqual(self.server.status['response'], 'success')


if __name__ == '__main__':
    unittest.main()
