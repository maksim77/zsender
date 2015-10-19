Zabbix Sender
=============

Quick Start
-----------

.. code-block:: python

    from ZabbixSender import ZabbixSender, ZabbixPacket
    server = ZabbixSender('127.0.0.1', 10051)
    packet = ZabbixPacket('myhost','key', 'value')
    server.send(packet)
    print(server.status)

::

    {'response': 'success', 'info': 'processed: 1; failed: 0; total: 1; seconds spent: 0.000297'}
