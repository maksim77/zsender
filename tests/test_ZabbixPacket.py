import unittest
from ZabbixSender import ZabbixPacket


class ZabbixPacketTests(unittest.TestCase):
    def test_packet_add_error(self):
        packet = ZabbixPacket()
        with self.assertRaises(TypeError):
            packet.add('host1', 'key1', 22.2, {'a': '1'})

    def test_clean(self):
        packet = ZabbixPacket()
        packet.add('host1', 'key1', 22.2)
        packet.clean()
        packet2 = ZabbixPacket()
        self.assertEqual(packet.__str__(), packet2.__str__())


