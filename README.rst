Zabbix Sender
=============
Quick Start
-----------
::
    from ZabbixSender import ZabbixSender, ZabbixPacket
    server = ZabbixSender('127.0.0.1', 10051)
    packet = ZabbixPacket('myhost','key', 'value')
    server.send(packet)
