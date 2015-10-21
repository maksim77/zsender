Zabbix Sender
=============

Quick Start
-----------

.. code:: python

    from ZabbixSender import ZabbixSender, ZabbixPacket
    server = ZabbixSender('127.0.0.1', 10051)
    packet = ZabbixPacket()
    packet.add('myhost','key', 'value')
    packet.add('myhost2', 'other_key', 'value2')
    server.send(packet)
    print(server.status)

::

    {'info': 'processed: 2; failed: 0; total: 4; seconds spent: 0.207659',
     'response': 'success'}
